from django.urls import path
from .views import all_products, in_sale

urlpatterns = [
    path("all-products/", all_products),
    path("in-sale/", in_sale)

]
