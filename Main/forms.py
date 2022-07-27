from django import forms
from .models import Airlines
class AirlinesForm(forms.ModelForm):
    class Meta:
        model=Airlines
        fields=("__all__")