from django import forms

from .models import Posts


class addPostForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
