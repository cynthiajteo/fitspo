from django import forms
# from django.forms import widgets
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('hidden', 'name',)

        widgets = {

            'workout': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Press enter for next set of exercise'
            }),
        }


class EditForm(forms.ModelForm):
    hidden = forms.BooleanField(label='Delete', required=False)

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('name',)

        widgets = {

            'workout': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Press enter for next set of exercise'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('name', 'post', 'hidden')

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment'})
        }


class LikeForm(forms.ModelForm):
    liked = forms.BooleanField(label='like')

    class Meta:
        model = Like
        fields = '__all__'
        # exclude = ('user', 'post',)
