from django.urls import path
from .views import (FoodCreateView,DrinkCreateView,SnacksCreateView,DessertCreateView,FoodDeleteView,FoodtListView,FoodUpdateView,DrinkDeleteView
,DrinkListView,DrinkUpdateView,SnacksDeleteView,SnacksListView,SnacksUpdateView,DessertDeleteView,DessertListView,DessertUpdateView)
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('food/food/new/', FoodCreateView.as_view(), name='food_new'),
    path('food/food/<int:pk>/delete/', FoodDeleteView.as_view(), name='food_delete'),
    path('food/food/list/', FoodtListView.as_view(), name='food_list'),
    path('food/food/<int:pk>/edit/',FoodUpdateView.as_view(), name='food_edit'),

    path('food/drink/new/', DrinkCreateView.as_view(), name='drink_new'),
    path('food/drink/<int:pk>/delete/', DrinkDeleteView.as_view(), name='drink_delete'),
    path('food/drink/list/', DrinkListView.as_view(), name='drink_list'),
    path('food/drink/<int:pk>/edit/',DrinkUpdateView.as_view(), name='drink_edit'),

    path('food/snacks/new/', SnacksCreateView.as_view(), name='snacks_new'),
    path('food/snacks/<int:pk>/delete/', SnacksDeleteView.as_view(), name='snacks_delete'),
    path('food/snacks/list/', SnacksListView.as_view(), name='snacks_list'),
    path('food/snacks/<int:pk>/edit/',SnacksUpdateView.as_view(), name='snacks_edit'),

    path('food/dessert/new/', DessertCreateView.as_view(), name='dessert_new'),
    path('food/dessert/<int:pk>/delete/', DessertDeleteView.as_view(), name='dessert_delete'),
    path('food/desser/list/', DessertListView.as_view(), name='dessert_list'),
    path('food/desser/<int:pk>/edit/',DessertUpdateView.as_view(), name='dessert_edit'),

    path('food/', TemplateView.as_view(template_name='add.html'), name='add'),

    
    
] 