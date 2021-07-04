from django.shortcuts import render

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
    return render(request, 'hw_register.html')


def login(request):
    return render(request, 'hw_login.html')


def logout(request):
    return render(request, 'logout.html')
