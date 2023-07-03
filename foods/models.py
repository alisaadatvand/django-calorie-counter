
from django.db import models
from django.urls import reverse

class foods(models.Model):
    name = models.CharField(("Food name"),max_length=200,blank=False,unique=True,null= True)
    cal = models.PositiveIntegerField(("Food calories"),help_text="Kcal",blank=False,null=True)
    
    
    def __str__(self):
        return str('{name} ({cal} Kcal)'.format(name=self.name, cal=self.cal))
    

    def get_absolute_url(self):
        return reverse("food_list")

class drink(models.Model):
    name = models.CharField(("Drink name"),max_length=200,blank=False,unique=True,null= True)
    cal = models.PositiveIntegerField(("Drink calories"),help_text="Kcal",blank=False,null=True)
    
    
    def __str__(self):
        return str('{name} ({cal} Kcal)'.format(name=self.name, cal=self.cal))
    

    def get_absolute_url(self):
        return reverse("drink_list")

class snacks(models.Model):
    name = models.CharField(("Snacks name"),max_length=200,blank=False,unique=True,null= True)
    cal = models.PositiveIntegerField(("Snacks calories"),help_text="Kcal",blank=False,null=True)

    def __str__(self):
        return str('{name} ({cal} Kcal)'.format(name=self.name, cal=self.cal))
    

    def get_absolute_url(self):
        return reverse("snacks_list")

class dessert(models.Model):
    name = models.CharField(("Dessert name"),max_length=200,blank=False,unique=True,null= True)
    cal = models.PositiveIntegerField(("Dessert calories"),help_text="Kcal",blank=False,null=True)
    
    
    def __str__(self):
        return str('{name} ({cal} Kcal)'.format(name=self.name, cal=self.cal))
    

    def get_absolute_url(self):
        return reverse("dessert_list")



    
    
    

