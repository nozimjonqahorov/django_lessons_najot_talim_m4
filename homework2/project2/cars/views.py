from django.shortcuts import render
from django.http import HttpResponse
from .models import Cars

def main_page(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


def all_cars(request):
    cars = Cars.objects.all()
    return  render(request, "cars.html", context={"cars": cars})