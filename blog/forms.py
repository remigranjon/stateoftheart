from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    
    class Meta :
        model = Article
        fields = ['title','domain', 'abstract', 'publishing_date', 'header_img', 'data']
        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Title', 'rows': 2}),
            'domain': forms.Select(attrs={'placeholder': 'Select the area of science'}),
            'abstract': forms.Textarea(attrs={'placeholder': 'Abstract'}),
        }