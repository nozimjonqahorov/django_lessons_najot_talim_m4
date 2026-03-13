from django.urls import path
from .views import show_books, saved_books, show_bestseller

urlpatterns = [
    path("all-books/", show_books),
    path("saved/", saved_books),
    path("bestsellers/", show_bestseller),
]
