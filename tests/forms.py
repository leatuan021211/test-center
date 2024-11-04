# yourapp/forms.py
from django import forms
from .models import Test, TestQuestion, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "instance" in kwargs:
            instance = kwargs["instance"]
            if instance and instance.limit_question:
                # Filter questions by the same category as the test
                self.fields["questions"] = forms.ModelMultipleChoiceField(
                    queryset=Question.objects.filter(category=instance.category),
                    required=False,
                    widget=forms.CheckboxSelectMultiple(),
                )
            else:
                self.fields["questions"] = forms.ModelMultipleChoiceField(
                    queryset=Question.objects.none(),
                    required=False,
                    widget=forms.CheckboxSelectMultiple(),
                )
        else:
            self.fields["questions"] = forms.ModelMultipleChoiceField(
                queryset=Question.objects.none(),
                required=False,
                widget=forms.CheckboxSelectMultiple(),
            )
