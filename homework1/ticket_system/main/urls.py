from django.urls import path
from .views import events, categories, login

urlpatterns = [
    path("events/", events),
    path("categories/", categories),
    path("login/", login)

]