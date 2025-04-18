from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.service}"
