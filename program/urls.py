from django.urls import path
from .views import (DietListView,DietDetailView,DietCreateView,DietUpdateView,DietDeleteView)

urlpatterns = [
    path('program/<int:pk>/delete/',DietDeleteView.as_view(), name='program_delete'),
    path('program/<int:pk>/edit/',DietUpdateView.as_view(), name='program_edit'),
    path('program/new/', DietCreateView.as_view(), name='program_new'), 
    path('program/<int:pk>/', DietDetailView.as_view(),name='program_detail'),
    path('', DietListView.as_view(), name='home'),
    
]