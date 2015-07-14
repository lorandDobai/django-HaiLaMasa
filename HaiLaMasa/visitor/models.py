from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Owner(User):
    phone = models.CharField(max_length=200)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Address(models.Model):
    street = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)

class Contact(models.Model):
    phone = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    restaurant = models.ForeignKey(Restaurant)

class Gallery(models.Model):
    picture = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)
