from django import forms
from page.models import Answer

class CommentForm(forms.ModelForm):
    title = forms.CharField(label='Введите своё имя')
    text = forms.Textarea(label='Оставить отзывб')
    
    class Meta:
        model = Answer    
        fields = ['title', 'text' ]