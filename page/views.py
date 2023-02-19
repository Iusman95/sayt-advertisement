from django.shortcuts import render
from page.models import Photo, Answer

# Create your views here.

def index(request):
    photo = Photo.objects.all()
    return render(request, 
        template_name='index.html', 
        context={'photo': photo}
        )


def index_two(request):
    photo_two = Photo.objects.all()
    return render(request, 
        template_name='index_two.html', 
        context={'photo_two': photo_two}
        )

def answer(request):
    
    answer = Answer.objects.all()
    if answer == answer:
        del answer
    return render(
        request,
        template_name=
    ) 

