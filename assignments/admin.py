from django.core.exceptions import ValidationError
from django.contrib import admin
from django.db import transaction
from questions.models import Question
from tests.models import TestQuestion
from .models import (
    Assignment,
    AssignmentQuestion,
    AssignmentMultiAnswer,
    AssignmentEssayAnswer,
    AssignmentFillBlankAnswer,
)
from .forms import AssignmentAdminForm


class AssignmentQuestionInline(admin.TabularInline):
    model = AssignmentQuestion
    extra = 0
    fields = (
        "question",
        "answer_display",
    )
    readonly_fields = ("question", "answer_display")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def answer_display(self, obj):
        answers = []

        if obj.question.question_type == "MA":
            answers = [
                f"Multi-Answer: {ma.answer} (Correct: {ma.is_correct})"
                for ma in obj.assignmentmultianswer_set.all()
            ]

        elif obj.question.question_type == "MC":
            answers = [
                f"Multi-Choice: {mc.answer} (Correct: {mc.is_correct})"
                for mc in obj.assignmentmultianswer_set.all()
            ]

        elif obj.question.question_type == "ES":
            answers = [
                f"Essay Answer: {ea.answer}"
                for ea in obj.assignmentessayanswer_set.all()
            ]

        elif obj.question.question_type == "FB":
            answers = [
                f"Fill-in-the-Blank Answer: {fba.position}: {fba.answer}"
                for fba in obj.assignmentfillblankanswer_set.all()
            ]

        return "\n".join(answers)

    answer_display.short_description = "Answers"


class AssignmentAdmin(admin.ModelAdmin):
    form = AssignmentAdminForm
    list_display = ("test", "assignee", "due_date", "created_at", "updated_at")
    search_fields = ("test__title", "assignee__username")
    list_filter = ("test", "assignee", "due_date")
    inlines = [AssignmentQuestionInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Select questions based on test configuration
        if obj.test.use_all_category:
            questions = Question.objects.filter(category=obj.test.category)
        else:
            questions = TestQuestion.objects.filter(test=obj.test).values_list(
                "question", flat=True
            )

        # Define required question counts
        num_essay = obj.test.num_essay_question
        num_mc = obj.test.num_multiple_choice_question
        num_ma = obj.test.num_multiple_answer_question
        num_fb = obj.test.num_fill_blank_question

        # Retrieve questions for each type
        essay_questions = list(
            questions.filter(question_type="ES").order_by("?")[:num_essay]
        )
        mc_questions = list(questions.filter(question_type="MC").order_by("?")[:num_mc])
        ma_questions = list(questions.filter(question_type="MA").order_by("?")[:num_ma])
        fb_questions = list(questions.filter(question_type="FB").order_by("?")[:num_fb])

        # Validate question availability
        if len(essay_questions) < num_essay:
            raise ValidationError(
                f"Not enough essay questions. Required: {num_essay}, Available: {len(essay_questions)}"
            )
        if len(mc_questions) < num_mc:
            raise ValidationError(
                f"Not enough multiple choice questions. Required: {num_mc}, Available: {len(mc_questions)}"
            )
        if len(ma_questions) < num_ma:
            raise ValidationError(
                f"Not enough multiple answer questions. Required: {num_ma}, Available: {len(ma_questions)}"
            )
        if len(fb_questions) < num_fb:
            raise ValidationError(
                f"Not enough fill in the blank questions. Required: {num_fb}, Available: {len(fb_questions)}"
            )

        # Remove old questions linked to this assignment
        obj.assignmentquestion_set.all().delete()

        # Add new questions
        with transaction.atomic():
            for question in (
                essay_questions + mc_questions + ma_questions + fb_questions
            ):
                AssignmentQuestion.objects.create(assignment=obj, question=question)

        obj.save()

    def get_queryset(self, request):
        qs = Assignment.objects.filter(test__created_by=request.user)
        return qs


class BaseAssignmentAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ("question", "answer", "created_at", "updated_at")
    fields = ("question", "answer", "score", "created_at", "updated_at")
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm(
            "assignments.delete_assignment"
        )


class AssignmentMultiAnswerAdmin(BaseAssignmentAnswerAdmin):
    list_display = ("question", "answer", "is_correct", "score", "created_at", "updated_at")
    search_fields = ("answer",)
    list_filter = ("is_correct",)


class AssignmentEssayAnswerAdmin(BaseAssignmentAnswerAdmin):
    list_display = ("question", "answer", "score", "created_at", "updated_at")
    search_fields = ("answer",)


class AssignmentFillBlankAnswerAdmin(BaseAssignmentAnswerAdmin):
    list_display = ("question", "position", "answer", "score", "created_at", "updated_at")
    search_fields = ("answer",)

    


# Register the admin class with the Assignment model
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AssignmentMultiAnswer, AssignmentMultiAnswerAdmin)
admin.site.register(AssignmentEssayAnswer, AssignmentEssayAnswerAdmin)
admin.site.register(AssignmentFillBlankAnswer, AssignmentFillBlankAnswerAdmin)
