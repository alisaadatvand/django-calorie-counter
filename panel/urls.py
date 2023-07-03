from django.urls import path
from .views import (PanelCreateView,PanelListView,PaneletailView,PanelUpdateView)

urlpatterns = [
   
    path('panel/<int:pk>/edit/',PanelUpdateView.as_view(), name='panel_edit'),
    path('panel/new/', PanelCreateView.as_view(), name='panel_new'), 
    path('panel/<int:pk>/', PaneletailView.as_view(),name='panel_detail'),
    path('panel/', PanelListView.as_view(), name='panel'),
]
