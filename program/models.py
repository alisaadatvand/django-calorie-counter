from django.db import models
from django.urls import reverse
import datetime

class program(models.Model):
    class Meals(models.TextChoices):
        Breakfast = 'Breakfast'
        Lunch = 'Lunch'
        Dinner = 'Dinner'


    title = models.CharField(max_length=200,blank=False)
    date = models.DateField(("Date"),default=datetime.date.today,blank=False)
    author = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE,blank=False,null=True)
    meal = models.CharField(max_length=200, choices=Meals.choices,blank=False,null=True)
    foods = models.ForeignKey('foods.foods', on_delete=models.CASCADE,null=True,blank=False)
    drinks = models.ForeignKey('foods.drink' , on_delete=models.CASCADE,null=True,blank=True)
    snacks = models.ForeignKey('foods.snacks' , on_delete=models.CASCADE,null=True,blank=True)
    dessert = models.ForeignKey('foods.dessert' , on_delete=models.CASCADE,null=True,blank=True)
    note = models.TextField(("Note"),max_length=300, null= True,blank=True)
     
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("program_detail", args=[str(self.id)])