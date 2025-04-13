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


def search_vendors(request):
    vendor_type = request.GET.get('vendor_type')
    city = request.GET.get('city')
    vendors = Vendor.objects.filter(vendor_type__iexact=vendor_type, city__iexact=city)
    return render(request, 'Home.html', {'vendors': vendors})
