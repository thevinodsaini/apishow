from unicodedata import name
from django.db import models

class Student(models.Model):
   name = models.CharField(max_length=50)
   city = models.CharField(max_length=50)
 
   
   
   

   