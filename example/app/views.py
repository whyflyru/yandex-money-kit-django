# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint

from django.views.generic import TemplateView
from yandex_money.forms import PaymentForm
from yandex_money.models import Payment
from .models import Goods, Order


class OrderPage(TemplateView):
    template_name = 'order_page.html'

    def get_context_data(self, **kwargs):
        goods, created = Goods.objects.get_or_create(name='Pen',
                                                     price=2)
        count = randint(1, 4)
        amount = count * goods.price

        payment = Payment(order_amount=amount)
        payment.save()

        order = Order(goods=goods, payment=payment,
                      count=count, amount=amount)
        order.save()

        ctx = super(OrderPage, self).get_context_data(**kwargs)
        ctx['form'] = PaymentForm(instance=payment)
        return ctx
