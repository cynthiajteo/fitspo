from django import forms
from django.forms import widgets
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'workout': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'add your workout here'
            }),
        }
