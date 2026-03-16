from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Bu sahifada Uzbekiston haqida eng so'nggi yangiliklar chop etiladi")

def weather_news(request):
    return HttpResponse("Bu sahifada Uzbekistion ob-havo yangiliklari ulashib boriladi! ")

def sport_news(request):
    return HttpResponse("Bu sahifada Uzbekiston sport yangiliklari ulashib boriladi! ")