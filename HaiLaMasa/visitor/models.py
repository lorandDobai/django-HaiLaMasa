from django.db import models
from mongoengine import *
from mongoengine.django.auth import User as MongoUser
# Create your models here.
class Address(EmbeddedDocument):
    city = StringField(max_length=50, required=True)
    street = StringField(max_length=50, required=True)
    building = StringField()
    coord = GeoPointField(required=True)


class Contact(EmbeddedDocument):
    phone = StringField(max_length=15)
    mail = EmailField()
    website = URLField()

class Menu(EmbeddedDocument):
    description = StringField()
    pret = DecimalField()
    picture = StringField()


class DailyMenu(EmbeddedDocument):
    date = DateTimeField()
    menus = ListField(EmbeddedDocumentField(Menu))


class Restaurant(Document):
    name = StringField(required=True)
    address = EmbeddedDocumentField(Address)
    gallery = ListField(StringField(max_length=30))
    contact = EmbeddedDocumentField(Contact)
    additional_info = StringField()
    daily_menu = ListField(EmbeddedDocumentField(DailyMenu))
    owner = ReferenceField(MongoUser)

# Create your models here.
