
from django import forms
from visitor.models import Restaurant

class LoginForm(forms.Form):
    username = forms.CharField(label='Nume utilizator', max_length=25)
    password = forms.CharField(label='Parola',widget = forms.PasswordInput())

class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurant