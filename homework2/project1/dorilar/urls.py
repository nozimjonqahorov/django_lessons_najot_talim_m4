from django.urls import path
from .views import main_page, about, contact, all_dorilar

urlpatterns = [
    path("", main_page, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name= "contact"),
    path("dorilar/", all_dorilar, name="dorilar"),
]
