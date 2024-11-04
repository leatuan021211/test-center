from django.contrib import admin
from .models import (
    Question,
    QuestionMultiAnswer,
    QuestionEssayAnswer,
    QuestionFillBlankAnswer,
)


class QuestionMultiAnswerInline(admin.TabularInline):
    model = QuestionMultiAnswer
    extra = 0


class QuestionEssayAnswerInline(admin.TabularInline):
    model = QuestionEssayAnswer
    extra = 0


class QuestionFillBlankAnswerInline(admin.TabularInline):
    model = QuestionFillBlankAnswer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "question_type", "category", "created_at", "updated_at")
    search_fields = ("text",)
    list_filter = ("question_type", "category", "created_at")
    ordering = ("-created_at",)
    exclude = ("created_by",)
    list_per_page = 10

    def get_inline_instances(self, request, obj=None):
        """Display only relevant answer inlines based on question_type."""
        inlines = []
        if obj:
            if obj.question_type == "MC" or obj.question_type == "MA":
                inlines.append(QuestionMultiAnswerInline(self.model, self.admin_site))
            elif obj.question_type == "ES":
                inlines.append(QuestionEssayAnswerInline(self.model, self.admin_site))
            elif obj.question_type == "FB":
                inlines.append(
                    QuestionFillBlankAnswerInline(self.model, self.admin_site)
                )
        return inlines


admin.site.register(Question, QuestionAdmin)
