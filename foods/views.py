from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic import ListView, UpdateView
from .models import foods,drink,snacks,dessert
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#Food
class FoodCreateView(LoginRequiredMixin,CreateView): 
    model = foods
    template_name = 'food_new.html'
    fields = ['name','cal']

class FoodDeleteView(LoginRequiredMixin,DeleteView): 
    model = foods
    template_name = 'food_delete.html'
    success_url = reverse_lazy('food_list')

class FoodtListView(LoginRequiredMixin,ListView):
    model = foods
    template_name = 'food_list.html'

class FoodUpdateView(LoginRequiredMixin,UpdateView): 
    model = foods
    template_name = 'food_edit.html'
    fields = ['name','cal']

#Drink

class DrinkCreateView(LoginRequiredMixin,CreateView):
    model = drink
    template_name = 'drink_new.html'
    fields = ['name','cal']

class DrinkDeleteView(LoginRequiredMixin,DeleteView): 
    model = drink
    template_name = 'drink_delete.html'
    success_url = reverse_lazy('drink_list')

class DrinkListView(LoginRequiredMixin,ListView):
    model = drink
    template_name = 'drink_list.html'

class DrinkUpdateView(LoginRequiredMixin,UpdateView): 
    model = drink
    template_name = 'drink_edit.html'
    fields = ['name','cal']

#Snacks
    
class SnacksCreateView(LoginRequiredMixin,CreateView):
    model = snacks
    template_name = 'snacks_new.html'
    fields = ['name','cal']

class SnacksDeleteView(LoginRequiredMixin,DeleteView): 
    model = snacks
    template_name = 'snacks_delete.html'
    success_url = reverse_lazy('snacks_list')

class SnacksListView(LoginRequiredMixin,ListView):
    model = snacks
    template_name = 'snacks_list.html'

class SnacksUpdateView(LoginRequiredMixin,UpdateView): 
    model = snacks
    template_name = 'snacks_edit.html'
    fields = ['name','cal']

#Dessert

class DessertCreateView(LoginRequiredMixin,CreateView):
    model = dessert
    template_name = 'dessert_new.html'
    fields = ['name','cal']

class DessertDeleteView(LoginRequiredMixin,DeleteView): 
    model = dessert
    template_name = 'dessert_delete.html'
    success_url = reverse_lazy('dessert_list')

class DessertListView(LoginRequiredMixin,ListView):
    model = dessert
    template_name = 'dessert_list.html'

class DessertUpdateView(LoginRequiredMixin,UpdateView): 
    model = dessert
    template_name = 'dessert_edit.html'
    fields = ['name','cal']







