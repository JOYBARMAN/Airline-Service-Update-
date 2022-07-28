from django import forms
from .models import Airlines,Flight_Book
class AirlinesForm(forms.ModelForm):
    class Meta:
        model=Airlines
        fields=("__all__")

class FlightBookForm(forms.ModelForm):
    class Meta:
        model=Flight_Book
        fields=("__all__")

