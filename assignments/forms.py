from django.contrib import admin
from .models import (
    Assignment,
    AssignmentQuestion,
    AssignmentMultiAnswer,
    AssignmentEssayAnswer,
    AssignmentFillBlankAnswer,
)
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class AssignmentAdminForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["test", "assignee", "due_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit("submit", "Save"))
