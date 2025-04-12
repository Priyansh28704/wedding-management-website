from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_vendors, name='search_vendors'),
    path('', views.home, name='search_vendors'), 
]
