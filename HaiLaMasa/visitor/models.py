from django.db import models
from mongoengine import *

# Create your models here.

class Restaurant(Document):
    name = StringField(required=True)

# Create your models here.
