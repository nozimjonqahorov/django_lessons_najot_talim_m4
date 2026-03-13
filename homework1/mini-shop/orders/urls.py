from django.urls import path
from .views import my_orders, cart

urlpatterns = [
    path("my-orders/", my_orders),
    path("cart/", cart),

]
