from django.urls import path
from .views import main_page, about, contact, all_cars

urlpatterns = [
    path("", main_page, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name= "contact"),
    path("cars/", all_cars, name="cars_list"),
    
]
