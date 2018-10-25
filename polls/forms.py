from django import forms
from .models import Post


class NameForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

