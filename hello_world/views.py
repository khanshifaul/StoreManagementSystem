from django import forms
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout
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

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'hw_register.html', context)


def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        print(request.POST)
    context = {}
    return render(request, 'hw_login.html', context)


def logout_view(request):
    logout(request)
