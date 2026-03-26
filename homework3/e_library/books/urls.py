from django.urls import path
from .views import *
urlpatterns = [
    path("", main_page, name="home"),    
    path("books/", books_list, name="books_list"),
    path("add-book/", add_book, name="add-book"),
    path("detail/<int:id>/", book_detail,  name="detail"),
    path("delete/<int:id>/", delete_book,  name="delete"),
    path("update/<int:id>/", update_book,  name="update"),

]
