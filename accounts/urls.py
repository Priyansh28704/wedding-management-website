from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import vendor_register



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('vendor-register/', vendor_register, name='vendor_register'),

]
