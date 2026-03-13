from django.urls import path
from .views import all_students, students_ranking

urlpatterns = [
    path("all-students/", all_students),
    path("ranking/", students_ranking),

]
