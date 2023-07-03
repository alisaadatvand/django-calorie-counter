from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView,BMIPageView

urlpatterns = [
    path('contact_me/', ContactPageView.as_view(), name= 'contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('bmi/', BMIPageView.as_view(),name='bmi'),


]

