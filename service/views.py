from django.shortcuts import render
from .models import Vendor

# Create your views here.
def home(request):
    vendors = None
    vendor_type = request.GET.get('vendor_type')
    city = request.GET.get('city')

    if vendor_type and city:
        vendors = Vendor.objects.filter(
            vendor_type__iexact=vendor_type,
            city__iexact=city
        )

    return render(request, 'Home.html', {'vendors': vendors})

from django.shortcuts import render
from .models import Vendor

def vendor_page(request):  # Fixed the function name
    return render(request, "vendor.html")

def search_vendors(request):
    if request.method == 'GET':
        vendor_type = request.GET.get('vendor_type')
        city = request.GET.get('city')

        vendors = Vendor.objects.all()  # Get all vendors

        if vendor_type and vendor_type != 'Select Vendor Type':
            vendors = vendors.filter(vendor_type=vendor_type)  # Filter by vendor_type

        if city and city != 'City':
            vendors = vendors.filter(city=city)  # Filter by city

        return render(request, 'home.html', {'vendors': vendors})

    return render(request, 'home.html')

