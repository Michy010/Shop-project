from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product (models.Model):
    ProductName = models.CharField (max_length=100)
    ActualPrice = models.DecimalField (max_digits=10 , decimal_places=2)
    Sold_Price = models.DecimalField (max_digits=10 , decimal_places=2)
    Discount = models.DecimalField (max_digits=10 , decimal_places=2)
    sold_At = models.DateField ()

    def __str__(self):
        return self.ProductName