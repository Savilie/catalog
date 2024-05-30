
from django.db import models
from django.utils.text import slugify
from pytils.translit import slugify as pytils_slugify
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

