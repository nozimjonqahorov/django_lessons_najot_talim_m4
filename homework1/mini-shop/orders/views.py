from django.shortcuts import render
from django.http import HttpResponse

def my_orders(request):
    return HttpResponse("Bu yerda foydalanuvchiuning aktiv va tugallangan zakazlari korsatiladi")

def cart(request):
    return HttpResponse("Bu yerda foydalanuvchiuning savatga qushgan mahsulotlari korsatiladi")

