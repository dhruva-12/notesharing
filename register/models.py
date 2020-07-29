# Create your models here.
from django.db import models
from django.contrib.auth.models import User


   # def __str__(self):
     #   return self.user.username

class Note(models.Model):
    sharewith = models.ManyToManyField(User, blank=True, null=True)
    subject = models.CharField(max_length=10, null=True)
    #date = models.DateTimeField()
    notesfile = models.FileField(upload_to='documents/',null=True)
    description = models.TextField(max_length=50,null=True)
   
#def __str__(self):
 # return self.sharewith.user.username

