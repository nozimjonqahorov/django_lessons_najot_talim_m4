from django.shortcuts import render
from django.http import HttpResponse

def profile(requast):
    return HttpResponse("Bu qismda user profile buladi")

def tickets(request):
    return HttpResponse("Bu sahifada user biletlarini korishingiz mumkin! ")
