from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Bu sahifada eng so'nggi dunyo yangiliklari chop etiladi")

def sport_news(request):
    return HttpResponse("Bu sahifada dunyo sport yangiliklari ulashib boriladi! ")