from django.db import models
from django.urls import reverse
import datetime

class panel(models.Model):

    Name = models.CharField(null=True,blank=False,max_length=50)
    age = models.PositiveIntegerField(null=True,blank=False)
    weight = models.FloatField(null=True,blank=False,help_text="Kg")
    height = models.FloatField(null=True,blank=False,help_text="m")
    date = models.DateField(("Date"),default=datetime.date.today,blank=False)
    
     
    

    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse("panel_detail", args=[str(self.id)])