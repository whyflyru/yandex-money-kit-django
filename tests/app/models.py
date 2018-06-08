# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField('Наименование', max_length=50)
    price = models.PositiveIntegerField('Стоимость')

    def __str__(self):
        return '%s %d' % (truncatechars(self.name, 8), self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Кол-во', default=1)
    payment = models.ForeignKey('yandex_money.Payment', verbose_name='Платеж', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
