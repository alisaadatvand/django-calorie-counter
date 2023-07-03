from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('program.urls')), 
    path('', include('foods.urls')),
    path('', include('accounts.urls')),
    path('', include('pages.urls')),
    path('', include('panel.urls')),
    path('', TemplateView.as_view(template_name='home.html'),
name='home'),
    
]
