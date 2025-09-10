from django import forms
from django.forms import ModelForm
from .models import Endereco

class ConsultaCepForm(forms.Form):
    cep = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={'placeholder': 'digite cep'})
    )
