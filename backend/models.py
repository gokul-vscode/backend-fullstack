from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title
