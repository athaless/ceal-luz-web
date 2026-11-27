from django import forms
from django.utils import timezone
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "email", "telefone", "data_nascimento"]
        widgets = {"data_nascimento": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})}

    def clean_data_nascimento(self):
        value = self.cleaned_data["data_nascimento"]
        if value and value > timezone.localdate():
            raise forms.ValidationError("A data de nascimento não pode estar no futuro.")
        return value
