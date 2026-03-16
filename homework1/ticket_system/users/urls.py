from django.urls import path
from .views import profile, tickets

urlpatterns = [
    path("profile/", profile),
    path("tickets/", tickets),
]