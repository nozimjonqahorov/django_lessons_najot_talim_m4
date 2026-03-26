from django.urls import path
from .views import *
urlpatterns = [
    path("", main_page, name="home"),    
    path("news/", news_list, name="list"),
    path("add-news/", add_news, name="add-news"),
    path("detail/<int:id>/", news_detail,  name="detail"),
    path("delete/<int:id>/", delete_news,  name="delete"),
    path("update/<int:id>/", update_news,  name="update"),

]
