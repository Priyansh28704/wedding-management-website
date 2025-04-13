from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service, Vendor  # ✅ Fixed import

from django.contrib.auth.forms import AuthenticationForm

def homePage(request):
    return render(request, "prinik.html")

def home(request):
    return render(request, "Home.html")

def Services(request):
    return render(request, "services.html")

def Venues(request):
    return render(request, "venues.html")

def Vendor(request):
    return render(request, "vendor.html")

def E_invitation(request):
    return render(request, "E-invitation.html")

def About_Us(request):
    return render(request, "About Us.html")

def register(request):
    return render(request, "register.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
       
        data = Service(username=username, password=password)  # ✅ Fixed model name
        data.save()

    return render(request, "login.html")

def search_vendors(request):
    if request.method == 'GET':
        vendors_type = request.GET.get('vendors_type')
        city = request.GET.get('city')

        vendors = Vendor.objects.all()

        if vendors_type and vendors_type != 'Select Vendor Type':
            vendors = vendors.filter(vendor_type=vendors_type)  # ✅ Fixed field name

        if city and city != 'City':
            vendors = vendors.filter(city=city)

        return render(request, 'home.html', {'vendors': vendors})

    return render(request, 'home.html')
