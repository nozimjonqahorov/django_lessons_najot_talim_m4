from django.urls import path
from .views import all_notebooks

urlpatterns = [
    path("", all_notebooks, name="notebooks"),
]