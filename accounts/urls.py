from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/password_change/', TemplateView.as_view(template_name='password_change_form.html'),name='paschange'),
]