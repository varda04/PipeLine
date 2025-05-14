from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect

app_name = 'customer'

urlpatterns = [
    path('', lambda request: redirect('customer:customer-login')),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='customer/login.html',
        redirect_authenticated_user=True  # if already logged in, go to dashboard
    ), name='customer-login'),

    path('signup/', views.customer_signup, name='customer-signup'),

    path('dashboard/', views.customer_dashboard, name='dashboard'),

    path('submit-request/', views.submit_request, name='request_form'),
    path('track-requests/', views.track_requests, name='request_status'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
