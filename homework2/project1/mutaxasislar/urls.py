from django.urls import path
from .views import main, all_mutaxasislar

urlpatterns = [
    path("", main, name="main"),
    path("mutaxasislar/", all_mutaxasislar, name="mutaxasislar"),
]
