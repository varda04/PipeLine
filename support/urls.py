from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('', lambda request: redirect('support:login')),
    path('login/', views.support_login, name='login'),
    path('dashboard', views.support_dashboard, name='dashboard'),
    path('update_status/<int:req_id>/', views.update_status, name='update_status'),
]