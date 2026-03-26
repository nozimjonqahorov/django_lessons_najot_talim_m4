from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

def main_page(request):
    return render(request, "index.html")

def books_list(request):

    all_books = Book.objects.all().order_by("-id") 
    # 2. Pass them to the template via the context dictionary
    return render(request, "books_list.html", {"books": all_books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_year = request.POST.get('published_year')
        isbn = request.POST.get('isbn')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')
        updated_at = request.POST.get('updated_at')
        
        
        
        books = Book( title = title,author =author, published_year = published_year, isbn = isbn, price = price, created_at = created_at, updated_at = updated_at,)
        books.save()
        
        return redirect('books_list')
        
    
    return render(request, 'add_book.html')

def book_detail(request, id):
    # book = Books.objects.get(id=id)
    # book = get_object_or_404(Books, id=id)
    book = Book.objects.filter(id = id).first()
    context = {
        "book": book
    }
    return render(request, "book_detail.html", context = context)

def delete_book(request, id):
    book = Book.objects.filter(id = id).first()
    if book:
        if request.method == "POST":
            book.delete()
            return redirect("books_list")
        context = {
            "book": book
        }
    return render(request, "delete_book.html", context = context)

def update_book(request, id):
    book = Book.objects.filter(id=id).first()
    
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_year = request.POST.get('published_year')
        book.isbn = request.POST.get('isbn')
        book.price = request.POST.get('price')
        book.created_at = request.POST.get('created_at')
        book.updated_at = request.POST.get('updated_at')
        book.save()
        return redirect('detail', book.id)
    
    context = {"book": book} 
    return render(request, 'update_book.html', context=context)