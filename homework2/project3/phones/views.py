from django.shortcuts import render
from django.http import HttpResponse
from .models import Phones

def all_phones(request):
    phones = Phones.objects.all()
    return render(request, "phones.html", context={"phones": phones})

