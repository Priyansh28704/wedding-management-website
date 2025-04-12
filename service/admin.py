from django.contrib import admin
from .models import Vendor, Service  # Correctly import Service model

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Vendor)
