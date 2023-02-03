from django import forms
from blog.models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

        labels = {
            'title': '제목',
            'body': '내용'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'body'}
        labels = {
            'body': '댓글내용',
        }