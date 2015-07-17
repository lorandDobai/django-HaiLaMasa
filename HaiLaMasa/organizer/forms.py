
from django import forms
from visitor.models import Restaurant, Menu

class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=25)
    password = forms.CharField(label='Parola',widget = forms.PasswordInput())

class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("city","name")

class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields =("description","picture","name","date","price")