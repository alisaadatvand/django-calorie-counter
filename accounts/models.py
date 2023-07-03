from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    Name = models.CharField(null=True,blank=False,max_length=50)
    cal = models.PositiveIntegerField(("Target calories"),help_text="Kcal",blank=False,null=True)
    


   



    
   