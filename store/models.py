

from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название магазина')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    seller = models.ForeignKey(Seller, related_name='items', on_delete=models.CASCADE, verbose_name='Продавец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    class Meta:
        ordering = ['-last_modified']

    def __str__(self):
        return self.name
