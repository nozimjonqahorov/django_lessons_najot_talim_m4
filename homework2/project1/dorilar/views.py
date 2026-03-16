from django.shortcuts import render
from django.http import HttpResponse
from .models import Dorilar

def main_page(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


def all_dorilar(request):
    dorilar = Dorilar.objects.all()
    return  render(request, "dorilar.html", context={"dorilar": dorilar})