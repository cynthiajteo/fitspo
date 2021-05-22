from django import forms
from django.forms import widgets
from comments.models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('name', 'post',)
