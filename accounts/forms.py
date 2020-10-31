from django import forms
from django.contrib.auth.models import User

class Signup_form(forms.Form):
    # CSS styles should not be inline. i've moved your style contents under a 'form-control' class
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type':'text', 'placeholder':'Username', 'name':'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email', 'placeholder':'Your E-mail', 'name':'email'}))
    password1 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password', 'name':'password1'}))
    password2 = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Confirm Password', 'name':'password2'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Login_form(forms.Form):
    # CSS styles should not be inline. i've moved your style contents under a 'form-control' class
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type':'text', 'placeholder':'Username', 'name':'username'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email', 'placeholder':'Your E-mail', 'name':'email'}))
    password = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'type':'password', 'placeholder':'Password', 'name':'password1'}))
    class Meta:
        model = User
        fields = ('username', 'password')
