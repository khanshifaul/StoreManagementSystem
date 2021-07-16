from django import forms
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
# Create your views here.


def index(request):
    return render(request, 'hw_index.html')


def features(request):
    return render(request, 'hw_features.html')


def pricing(request):
    return render(request, 'hw_pricing.html')


def faqs(request):
    return render(request, 'hw_faqs.html')


def about(request):
    return render(request, 'hw_about.html')


def register(request):
    form = UserRegisterForm()
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'hw_register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'username or password is incorrect')
                return render(request, 'hw_login.html')

    context = {}
    return render(request, 'hw_login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
