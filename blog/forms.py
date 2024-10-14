from django import forms
from .models import Comment, Post
from taggit.forms import TagField


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', required=True,
                            widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Название поста'}))
    body = forms.CharField(label='Текст поста', required=True,
                           widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Введите текст'}))
    tags = TagField(label='Tags', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Введите теги через запятую'}))

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True,
                           widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Имя'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Ваш E-Mail'}))
    to = forms.EmailField(required=True,
                          widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Кому'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Комментарий'}))


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Комментарий', required=True,
                           widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Введите текст'}))

    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    query = forms.CharField(label='Искать', widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите поисковый запрос...'}))
