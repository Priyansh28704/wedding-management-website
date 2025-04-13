from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from service.models import Service, Vendor

# Home Page view
def homePage(request):
    return render(request, "prinik.html")

# Default home page after login
def home(request):
    return render(request, "Home.html")

# Services page view
def Services(request):
    return render(request, "services.html")

# Venues page view
def Venues(request):
    return render(request, "venues.html")

# Vendor page view
def Vendor(request):
    return render(request, "vendor.html")

# E-invitation page view
def E_invitation(request):
    return render(request, "E-invitation.html")

# About Us page view
def About_Us(request):
    return render(request, "About Us.html")

# Register page view
def register(request):
    return render(request, "register.html")

# Login view to handle user authentication
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Login the user
            return redirect('home')  # Redirect to home after successful login
        else:
            # Invalid login credentials handling
            return render(request, "login.html", {'error': 'Invalid username or password'})

    return render(request, "login.html")

# Search vendors based on vendor type and city
def search_vendors(request):
    if request.method == 'GET':
        vendors_type = request.GET.get('vendors_type')
        city = request.GET.get('city')

        vendors = Vendor.objects.all()

        if vendors_type and vendors_type != 'Select Vendor Type':
            vendors = vendors.filter(vendor_type=vendors_type)  # Fixed field name

        if city and city != 'City':
            vendors = vendors.filter(city=city)

        return render(request, 'home.html', {'vendors': vendors})

    return render(request, 'home.html')
