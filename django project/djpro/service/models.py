from django.db import models

class service(models.Model):
    username= models.CharField(max_length=255)
    password = models.CharField(max_length=100)

    

# models.py
from django.db import models

class Vendors(models.Model):
    VENDORS_TYPES = [
        ('Banquet Halls', 'Banquet Halls'),
        ('Wedding Resorts', 'Wedding Resorts'),
        ('Destination Wedding Venues', 'Destination Wedding Venues'),
        ('4 Star & Above Wedding Hotels', '4 Star & Above Wedding Hotels'),
        ('Venue Concierge services', 'Venue Concierge services'),
        ('Small function & Party Halls', 'Small function & Party Halls'),
        ('View all Venues', 'View all Venues'),
    ]
    
    vendors_type = models.CharField(max_length=100, choices=VENDORS_TYPES)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
