from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_two/', views.index_two),
]