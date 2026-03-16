from django.shortcuts import render
from django.http import HttpResponse
from .models import Motos

def main(request):
    return render(request, "main.html")


def all_motos(request):
    motos = Motos.objects.all()
    return  render(request, "motos.html", context={"motos": motos})