from django.urls import path
from .views import all_courses, user_courses

urlpatterns = [
    path("all-courses/", all_courses),
    path("user-courses/", user_courses),

]
