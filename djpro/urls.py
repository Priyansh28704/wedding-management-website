from django.contrib import admin
from django.urls import path, include
from djpro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Custom register
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout
    path('chatbot/', include('chatbot.urls')),
    path('', views.homePage, name="homePage"),  
    path('Home', views.home, name="Home"),
    path('services/', views.Services, name="services"),
    path('venues', views.Venues, name="venues"),
    path('vendor', views.vendor_page, name="vendor_page"),  # Vendor page link
    path('E-invitation', views.E_invitation, name="E-invitation"),
    path('About Us', views.About_Us, name="About Us"),
    path('userform', views.Login, name="userform"),
    path('search/', views.search_vendors, name='search_vendors'),  # Search page
]
