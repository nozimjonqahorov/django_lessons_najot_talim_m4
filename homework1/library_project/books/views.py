from django.shortcuts import render
from django.http import HttpResponse


def show_books(request):
    return HttpResponse("Bu yerda barcha kitoblarni korishingiz mumkin! ")


def saved_books(request):
    return HttpResponse("Bu yerda saqlangan kitoblarni korishingiz mumkin! ")


def show_bestseller(request):
    return HttpResponse("Bu sahifada eng kop uqilgan kitoblar mavjud")
