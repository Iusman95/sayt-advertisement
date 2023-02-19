from django.db import models

# Create your models here.



class Photo(models.Model):
    photo = models.FileField(upload_to='photo/')



class Answer(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=600)
    time = models.DateTimeField(auto_now_add=True)


    