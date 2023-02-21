from django import forms
from page.models import Answer

class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer    
        fields = ['title', 'text' ]