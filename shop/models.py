from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    price = models.FloatField()
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=200)
    stock = models.IntegerField()
    shop_location = models.TextField()
    date_posted = models.DateTimeField(blank=True, null=True)

    def add_item(self):
        self.date_posted = timezone.now()
        self.save()

    def remove_item(self):
        self.delete()

    def __str__(self):
        return self.description
