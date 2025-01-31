from django.contrib.auth.models import User 
from .models import Product , Restaurant ,Author , Blog
from django.contrib.auth.forms import UserCreationForm  , AuthenticationForm
from django import forms
from django.forms.widgets import TextInput , PasswordInput


class ProductForms(forms.ModelForm):
    class Meta :
        model= Product
        fields = '__all__'


class RestaurantForms(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields= '__all__'



class AuthorForm(forms.ModelForm):
    class Meta :
        model = Author
        fields = '__all__'


class CreateUser(UserCreationForm) :

    class Meta:
        model = User
        fields= ['username' ,'email' , 'password1' , 'password2']


class LoginUser(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
        



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'