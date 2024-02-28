# Generated by Django 5.0.2 on 2024-02-28 10:16

from django.db import migrations
from store.models import Seller, Item

def add_data(apps, schema_editor):
    Seller = apps.get_model('store', 'Seller')
    Item = apps.get_model('store', 'Item')

    # Добавляем данные для модели Seller
    Seller.objects.bulk_create([
        Seller(name='Магазин 1', description='Описание магазина 1'),
        Seller(name='Магазин 2', description='Описание магазина 2'),
        Seller(name='Магазин 3', description='Описание магазина 3'),
    ])

    # Добавляем данные для модели Item
    Item.objects.bulk_create([
        Item(name='Товар 1', description='Описание товара 1', seller_id=1),
        Item(name='Товар 2', description='Описание товара 2', seller_id=2),
        Item(name='Товар 3', description='Описание товара 3', seller_id=3),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]
