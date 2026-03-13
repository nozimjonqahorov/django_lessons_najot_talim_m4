from django.shortcuts import render
from django.http import HttpResponse

def all_products(request):
    return HttpResponse("Bu qismda barcha mahsulotlarni korishingiz mukin")

def in_sale(request):
    return HttpResponse("Bu yerda chegirmadagi mahsulotlar korinadi")


