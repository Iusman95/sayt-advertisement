from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_two/', views.answer, name='answer'),
    path('grants/', views.stipendia, name='stipendia'), 
]