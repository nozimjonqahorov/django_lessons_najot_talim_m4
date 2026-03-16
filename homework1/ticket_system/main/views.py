from django.shortcuts import render
from django.http import HttpResponse

def events(requast):
    return HttpResponse("Bu qismda barcha tadbirlar ruyxati buladi")

def categories(request):
    return HttpResponse("Bu sahifada kategoriya buyicha tadbirlarni korishingiz mumkin! ")

def login(request):
    return HttpResponse("Bu sahifada userlar log in qilishlari mumkin")