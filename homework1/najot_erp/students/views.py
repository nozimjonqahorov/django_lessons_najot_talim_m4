from django.shortcuts import render
from django.http import HttpResponse

def all_students(request):
    return HttpResponse("Bu sahifada barcha uquvchilarni ko'rishingiz mumkin! ")

def students_ranking(request):
    return HttpResponse("Bu sahifada uquvchilar statistikasini korishingiz mumkin!  ")