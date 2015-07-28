from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Owner(User):
    phone = models.CharField(max_length=200)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, default=0.0)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, default=0.0)
    restaurant = models.ForeignKey(Restaurant)


class Contact(models.Model):
    phone = models.CharField(max_length=200, blank=True)
    mail = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.restaurant.name


class Menu(models.Model):
    menu_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.menu_name


class Gallery(models.Model):
    picture = models.ImageField(upload_to='static/images')
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.restaurant.name
