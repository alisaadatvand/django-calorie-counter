from django.views.generic import ListView, DetailView 
from django.views.generic.edit import (CreateView, UpdateView, DeleteView) 
from django.urls import reverse_lazy
from .models import program
from django.contrib.auth.mixins import LoginRequiredMixin


class DietListView(LoginRequiredMixin,ListView):
    model = program
    template_name = 'home.html'

class DietDetailView(LoginRequiredMixin,DetailView): 
    model = program
    template_name = 'program_detail.html'

class DietCreateView(LoginRequiredMixin,CreateView): 
    model = program
    template_name = 'program_new.html'
    fields = ['title', 'date','author','meal','foods','drinks','snacks','dessert','note']

class DietUpdateView(LoginRequiredMixin,UpdateView): 
    model = program
    template_name = 'program_edit.html'
    fields = ['title','meal','foods','drinks','snacks','dessert','note']

class DietDeleteView(LoginRequiredMixin,DeleteView): 
    model = program
    template_name = 'program_delete.html'
    success_url = reverse_lazy('home')


