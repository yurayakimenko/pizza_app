from django import forms
from .models import Order


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)