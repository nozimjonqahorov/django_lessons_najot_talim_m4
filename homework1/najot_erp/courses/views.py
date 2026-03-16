from django.shortcuts import render
from django.http import HttpResponse

def all_courses(request):
    return HttpResponse("Bu sahifada barcha kurslarni ko'rishingiz mumkin! ")

def user_courses(request):
    return HttpResponse("Bu sahifada mijozning tugatgan yoki hozir uqiyotgan kurslari chiqadi")
