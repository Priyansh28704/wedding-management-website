from django.contrib import admin
from django.urls import path, include
from djpro import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # custom register
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('', lambda request: redirect('login')),  # Root URL redirects to login page
    path('main/', include('djpros.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('services/', views.Services, name="services"),
    path('venues/', views.Venues, name="venues"),
    path('vendor/', views.Vendor, name="vendor"),
    path('E-invitation/', views.E_invitation, name="E-invitation"),
    path('About Us/', views.About_Us, name="About Us"),
    path('userform/', views.Login, name="userform"),
    path('search_vendors/', views.search_vendors, name='search_vendors'),
    path('home/', views.home, name="home"),  # Home page after login
]
