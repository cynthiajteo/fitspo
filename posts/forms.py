from django import forms
from django.forms import widgets
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('hidden', 'name',)

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
    hidden = forms.BooleanField(label='delete', required=False)

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('name',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('name', 'post',)

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'comment'})
        }
