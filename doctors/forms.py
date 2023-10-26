from django import forms
from .models import Footballer


class FestivalForm(forms.ModelForm):
    class Meta:
        model = Footballer
        fields = [
            "name",
            "price",
            "age",
        ]