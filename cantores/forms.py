from django import forms
from .models import Cantores

class CantoresForm(forms.ModelForm):
    class Meta:
        model = Cantores
        fields = ['nome','estilos']