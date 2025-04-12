from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vendor_type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image_url = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

# Dummy Service model added for admin reference (replace or update if needed)
class Service(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

