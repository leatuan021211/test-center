from django.db import models
from django.conf import settings
from tests.models import Test
from questions.models import Question


class Assignment(models.Model):
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "assignments"

    def __str__(self) -> str:
        return f"{self.test} - {self.assignee}"


class AssignmentQuestion(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "assignment_questions"

    def __str__(self) -> str:
        return f"{self.id} - {self.assignment.assignee} - {self.question.text[:50]}{'. . .' if len(self.question.text) > 50 else ''}"


class BaseAnswer(models.Model):
    question = models.ForeignKey(AssignmentQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class AssignmentMultiAnswer(BaseAnswer):
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "assignment_multi_answers"

    def __str__(self) -> str:
        return f"{self.answer}"


class AssignmentEssayAnswer(BaseAnswer):

    class Meta:
        db_table = "assignment_essay_answers"

    def __str__(self) -> str:
        return f"{self.answer}"


class AssignmentFillBlankAnswer(BaseAnswer):
    position = models.PositiveIntegerField()

    class Meta:
        db_table = "assignment_fill_blank_answers"

    def __str__(self) -> str:
        return f"{self.answer}"
