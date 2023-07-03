from django.views.generic import ListView, DetailView 
from django.views.generic.edit import (CreateView, UpdateView) 
from django.urls import reverse_lazy
from .models import panel
from django.contrib.auth.mixins import LoginRequiredMixin

class PanelListView(LoginRequiredMixin,ListView):
    model = panel
    template_name = 'panel.html'

class PaneletailView(LoginRequiredMixin,DetailView): 
    model = panel
    template_name = 'panel_detail.html'

class PanelCreateView(LoginRequiredMixin,CreateView): 
    model = panel
    template_name = 'panel_new.html'
    fields = ['date','Name', 'age','height','weight']

class PanelUpdateView(LoginRequiredMixin,UpdateView): 
    model = panel
    template_name = 'panel_edit.html'
    fields = ['Name', 'age','height','weight']





