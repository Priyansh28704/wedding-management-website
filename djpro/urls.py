from django.contrib import admin
from django.urls import path,include
from djpro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # custom register
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    #path('', include('service.urls')),
    path('chatbot/',include('chatbot.urls')),
    path('', views.homePage, name="homePage"),  
    path('Home', views.home, name="Home"),
    path('services/', views.Services, name="services"),
    path('venues', views.Venues, name="venues"),
    path('vendor', views.Vendor, name="vendor"),
    path('E-invitation', views.E_invitation, name="E-invitation"),
    path('About Us', views.About_Us, name="About Us"),
    path('userform', views.Login,name="userform"),
    #path('register', views.register,name="register"),
   #path('saveenquiry', views.Saveenquiry, name="saveenquiry"),
    path('', views.search_vendors, name='search_vendors'),
]
