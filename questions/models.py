from django.db import models
from django.conf import settings
from categories.models import Category


class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ("MC", "Multiple Choice"),
        ("ES", "Essay"),
        ("MA", "Multiple Answer"),
        ("FB", "Fill in the Blank"),
    ]

    text = models.TextField(max_length=1000)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "questions"

    def __str__(self):
        return f"{self.text}"


class BaseQuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class QuestionMultiAnswer(BaseQuestionAnswer):
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = "question_multi_answers"

    def __str__(self) -> str:
        return f"{self.question}\n{self.answer} - {self.is_correct}"


class QuestionEssayAnswer(BaseQuestionAnswer):

    class Meta:
        db_table = "question_essay_answers"

    def __str__(self) -> str:
        return f"{self.question}\n{self.answer}"


class QuestionFillBlankAnswer(BaseQuestionAnswer):
    position = models.PositiveIntegerField()

    class Meta:
        db_table = "question_fill_blank_answers"

    def __str__(self) -> str:
        return f"{self.question}\n{self.position}: {self.answer}"
