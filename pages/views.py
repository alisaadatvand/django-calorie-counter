from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'


class AboutPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'
    

class ContactPageView(LoginRequiredMixin,TemplateView):
    template_name = 'contact.html'

class BMIPageView(LoginRequiredMixin,TemplateView):
    template_name = 'bmi.html'

