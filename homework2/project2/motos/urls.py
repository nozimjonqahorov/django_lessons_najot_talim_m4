from django.urls import path
from .views import main, all_motos

urlpatterns = [
    path("", main, name="main"),
    path("motos/", all_motos, name="motos_list"),
]
