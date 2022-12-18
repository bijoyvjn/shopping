from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password1 = request.POST.get('password1')
            data.password2 = request.POST.get('password2')
            data.is_staff = True
            data.save()
            messages.success(request, 'New User Successfully Created', 'alert-success')
            return redirect('login')
        else:
            messages.success(request, 'Invalid Data', 'alert-danger')
    else:
        form = UserRegForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {'msg': 'Invalid Username or Password'}
            # return render(request, "frontend/signin.html", context)
            return render(request, "registration/login.html", context)
    else:
        return render(request, "registration/login.html")
