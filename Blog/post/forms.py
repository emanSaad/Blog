from django.db.models import fields
from .models import *
from django import forms
from django.forms import ModelForm, Textarea
from .models import Post

class createPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields =['title','content', 'author', 'status']
        # widget ={
        #     'content': Textarea(attrs = {
        #         'cols':80,
        #         'rows':20
        #     }),
        # }