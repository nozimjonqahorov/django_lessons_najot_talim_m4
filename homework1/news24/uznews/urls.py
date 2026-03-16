from django.urls import path
from .views import main, weather_news, sport_news

urlpatterns = [
    path("main/", main),
    path("weather/", weather_news),
    path("sport/", sport_news)

]
