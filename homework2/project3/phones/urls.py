from django.urls import path
from .views import all_phones

urlpatterns = [
    path("", all_phones, name="phones"),
]