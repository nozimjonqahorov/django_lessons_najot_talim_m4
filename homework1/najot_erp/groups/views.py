from django.shortcuts import render
from django.http import HttpResponse

def all_groups(request):
    return HttpResponse("Bu sahifada barcha guruhlarni ko'rishingiz mumkin! ")

def user_groups(request):
    return HttpResponse("Bu sahifada user bitirgan yoki hozir uqiyotgan gurihlari chiqadi")

