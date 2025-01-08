from django.http import HttpResponse
from django.shortcuts import render
from service.models import service
from django.contrib.auth.forms import AuthenticationForm
def homePage(request):
    
    return render(request,"prinik.html")
def home(request):
    
    return render(request,"Home.html")

def Services(request):
    
    return render(request,"services.html")

def Venues(request):
    
    return render(request,"venues.html")

def Vendor(request):
    
    return render(request,"vendor.html")

def E_invitation(request):
    
    return render(request,"E-invitation.html")

def About_Us(request):
    
    return render(request,"About Us.html")
def register(request):
    
    return render(request,"register.html")


def Login(request):
    if request.method == "POST":
       username = request.POST.get('username') 
       password = request.POST.get('password') 
       #submit= request.POST.get('submit') 
      
       
       data =service(username=username, password=password)
       data.save()
    return render(request,"userform.html")


# views.py
from django.shortcuts import render
from service.models import Vendors

def search_vendors(request):
    if request.method == 'GET':
        # Get vendor_type and city from the GET parameter
        vendors_type = request.GET.get('vendors_type')
        city = request.GET.get('city')

        # Filter vendors based on the selected vendor_type and city
        vendors = Vendors.objects.all()  # Start with all vendors

        if vendors_type and vendors_type != 'Select Vendor Type':
            vendors = vendors.filter(vendors_type=vendors_type)
        
        if city and city != 'City':
            vendors = vendors.filter(city=city)

        # Return the filtered vendor results to the template
        return render(request, 'home.html', {'vendors': vendors})

    return render(request, 'home.html')













