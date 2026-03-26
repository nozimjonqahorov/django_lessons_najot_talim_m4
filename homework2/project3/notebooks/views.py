from django.shortcuts import render
from django.http import HttpResponse
from .models import Notebooks
from django.shortcuts import redirect

def all_notebooks(request):
    notebooks = Notebooks.objects.all()
    return render(request, "notebooks.html", context={"notebooks": notebooks})

def add_notebook(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        model_name = request.POST.get('model_name')
        processor = request.POST.get('processor')
        ram = request.POST.get('ram')
        storage = request.POST.get('storage')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        
        n_book = Notebooks(brand = brand, model_name = model_name, processor = processor, ram = ram, storage = storage, price = price, stock = stock)
        n_book.save()
        
        return redirect('notebooks')
        
    
    return render(request, 'add_notebook.html')
