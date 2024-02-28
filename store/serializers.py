

from rest_framework import serializers
from .models import Seller, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'seller', 'created_at', 'last_modified']
        read_only_fields = ['id', 'created_at', 'last_modified']

class SellerSerializer(serializers.ModelSerializer):
    num_items = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ['id', 'name', 'description', 'created_at', 'num_items']
        read_only_fields = ['id', 'created_at', 'num_items']

    def get_num_items(self, obj):
        return obj.items.count()
