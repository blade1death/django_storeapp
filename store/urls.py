# urls.py

from django.urls import path
from .views import SellerListView, SellerDetailView, ItemDetailView

urlpatterns = [
    path('sellers/', SellerListView.as_view(), name='seller-list'),
    path('sellers/<int:id>/', SellerDetailView.as_view(), name='seller-detail'),
    path('items/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
]
