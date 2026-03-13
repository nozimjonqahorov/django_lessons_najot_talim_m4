from django.urls import path
from .views import main, sport_news

urlpatterns = [
    path("main/", main),
    path("sport/", sport_news)

]
