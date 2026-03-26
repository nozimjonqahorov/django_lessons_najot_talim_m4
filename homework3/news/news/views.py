from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.shortcuts import redirect

def main_page(request):
    return render(request, "index.html")

def news_list(request):

    all_news = News.objects.all().order_by("-id") 
    # 2. Pass them to the template via the context dictionary
    return render(request, "news_list.html", {"news": all_news})

def add_news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        country = request.POST.get('country')
        desc = request.POST.get("desc")
        
        
        news = News( title = title,author =author, country = country, desc = desc)
        news.save()
        
        return redirect('list')
        
    
    return render(request, 'add_news.html')

def news_detail(request, id):
    
    news = News.objects.filter(id = id).first()
    context = {
        "news": news
    }
    return render(request, "news_detail.html", context = context)

def delete_news(request, id):
    news = News.objects.filter(id = id).first()
    if news:
        if request.method == "POST":
            news.delete()
            return redirect("list")
        context = {
            "news": news
        }
    return render(request, "delete_news.html", context = context)

def update_news(request, id):
    news = News.objects.filter(id=id).first()
    
    if request.method == "POST":
        news.title = request.POST.get('title')
        news.author = request.POST.get('author')
        news.country = request.POST.get('country')
        news.desc = request.POST.get('desc')
     
        news.save()
        return redirect('detail', news.id)
    
    context = {"news": news} 
    return render(request, 'update_news.html', context=context)