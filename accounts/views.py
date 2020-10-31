from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . import forms
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_req(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
        form = forms.Login_form()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        form = forms.Login_form()
        return render(request, 'accounts/login.html', {'form': form})

    
def register(request):
    if request.method == 'POST':

        username = request.POST.get('username','')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 == password2:
            user = User.objects.create_user(username=username,email=email, password=password1)
            if user:
                user.save()

            return redirect('/')
        else:
            pass
    else:
        form = forms.Signup_form()
        return render(request, 'accounts/register.html', {'form' : form})

    
def profile(request):
    return render(request, 'accounts/profile.html')