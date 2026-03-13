from django.urls import path
from .views import all_groups, user_groups

urlpatterns = [
    path("all-courses/", all_groups),
    path("user-courses/", user_groups),

]
