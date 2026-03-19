from django.shortcuts import render
from django.http import HttpResponse
from .models import Notebooks
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

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



def notebook_detail(request, id):
    notebook = get_object_or_404(Notebooks, id=id)

    return render(request, "notebook_detail.html", {"notebook": notebook})

def notebook_delete(request, id):
    notebook = Notebooks.objects.filter(id=id).first()
    if request.method == "POST":
        if notebook:
            notebook.delete()
            return redirect('notebooks')
        
    context = {
        'notebook': notebook
    }
    
    return render(request, 'notebook_delete.html', context=context)


def update_notebook(request, id):
    notebook = Notebooks.objects.filter(id=id).first()

    if request.method == "POST":
        notebook.brand = request.POST.get('brand')
        notebook.model_name = request.POST.get('model_name')
        notebook.processor = request.POST.get('processor')
        notebook.ram = request.POST.get('ram')
        notebook.storage = request.POST.get('storage')
        notebook.price = request.POST.get('price')
        notebook.stock = request.POST.get('stock')
        notebook.save()
        
        return redirect('detail', notebook.id)
        
    
    return render(request, 'update.html', context={'notebook': notebook})