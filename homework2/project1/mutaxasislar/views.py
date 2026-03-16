from django.shortcuts import render
from django.http import HttpResponse
from .models import Mutaxasislar

def main(request):
    return render(request, "main.html")


def all_mutaxasislar(request):
    mutaxasislar = Mutaxasislar.objects.all()
    return  render(request, "mutaxasislar.html", context={"mutaxasislar": mutaxasislar})