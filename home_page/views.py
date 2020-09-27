from pprint import pprint

from django.shortcuts import render


# Create your views here

def index(request):
    return render(request, 'home_page/index.html')


def portfolio(request):
    return render(request, 'home_page/portfolio.html')


def services(request):
    return render(request, 'home_page/services.html')


def resume(request):
    return render(request, 'home_page/resume.html')


def contact(request):
    return render(request, 'home_page/contact.html')
