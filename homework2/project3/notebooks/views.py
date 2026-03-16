from django.shortcuts import render
from django.http import HttpResponse
from .models import Notebooks

def all_notebooks(request):
    notebooks = Notebooks.objects.all()
    return render(request, "notebooks.html", context={"notebooks": notebooks})

