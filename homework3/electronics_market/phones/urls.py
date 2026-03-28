from django.urls import path
from .views import PhonesListView, PhoneCreateView, PhoneUpdateView, PhoneDeleteView, PhoneDetailView
urlpatterns = [
    path('', PhonesListView.as_view(), name='phones_list'),
    path('detail/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('add/', PhoneCreateView.as_view(), name='phone_add'),
    path('edit/<int:pk>/', PhoneUpdateView.as_view(), name='phone_edit'),
    path('delete/<int:pk>/', PhoneDeleteView.as_view(), name='phone_delete'),
]