from django.shortcuts import render, redirect
from page.models import Photo, Answer
from page.forms import AnswerForm
from django.urls import reverse


# Create your views here.

def index(request):
    photo = Photo.objects.all()
    return render(request, 
        template_name='index.html', 
        context={'photo': photo}
        )



def answer(request):
    answer_form = AnswerForm()

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
    
    
    context = {
        'form': answer_form
        }

    return render(
        request,
        template_name='index_two.html', 
        context = context 
        ) 

   

        
