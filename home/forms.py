from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', "body"]

        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Название поста"}),
            "body": forms.Textarea(attrs={"placeholder": "Описание поста"})
        }