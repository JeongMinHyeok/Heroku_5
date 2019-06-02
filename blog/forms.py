from django import forms
from .models import Blog, Comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body', 'hashtags', 'media']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']