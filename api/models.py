from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    # id =models.CharField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name
