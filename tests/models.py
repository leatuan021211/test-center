from django.conf import settings
from django.db import models
from categories.models import Category
from questions.models import Question


class Test(models.Model):
    title = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    description = models.TextField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    use_all_category = models.BooleanField(default=False)
    num_essay_question = models.PositiveIntegerField(default=0)
    num_multiple_choice_question = models.PositiveIntegerField(default=0)
    num_multiple_answer_question = models.PositiveIntegerField(default=0)
    num_fill_blank_question = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tests"

    def __str__(self):
        return f"{self.title}"


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = "test_questions"

    def __str__(self):
        return f"{self.question.text[:100] + '...' if len(self.question.text) >= 100 else self.question.text}"
