from django.shortcuts import render
from page.models import Photo

# Create your views here.

def index(request):
    photo = Photo.objects.all()
    return render(request, 
        template_name='index.html', 
        context={'photo': photo}
        )

