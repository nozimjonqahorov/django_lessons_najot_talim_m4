from django.urls import path
from .views import all_notebooks, add_notebook, notebook_detail, update_notebook, notebook_delete

urlpatterns = [
    path("", all_notebooks, name="notebooks"),
    path("add/", add_notebook, name = "add"),
    
    path('detail/<int:id>', notebook_detail, name='detail'),
    path('delete/<int:id>', notebook_delete, name='delete'),
    path('update/<int:id>', update_notebook, name='update'),
]
