# views.py

from rest_framework import generics
from .models import Seller, Item
from .serializers import SellerSerializer, ItemSerializer

class SellerListView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SellerDetailView(generics.RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'id'

class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

