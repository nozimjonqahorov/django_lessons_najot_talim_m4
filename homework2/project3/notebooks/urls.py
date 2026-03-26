from django.urls import path
from .views import all_notebooks, add_notebook

urlpatterns = [
    path("", all_notebooks, name="notebooks"),
    path("add/", add_notebook, name = "add")
]