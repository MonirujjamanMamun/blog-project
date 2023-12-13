from django import forms

from .models import Categores


class addCategoresForms(forms.ModelForm):
    class Meta:
        model = Categores
        fields = '__all__'
