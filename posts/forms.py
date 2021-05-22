from django import forms
from django.forms import widgets
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('hidden',)

        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'workout': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'add your workout here'
            }),
        }


class EditForm(forms.ModelForm):
    hidden = forms.BooleanField(label='delete')

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('name',)
