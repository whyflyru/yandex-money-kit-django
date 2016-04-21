# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.utils import override_settings
from django import forms

from models import Product, Order
from yandex_money.models import Payment
from yandex_money.forms import PaymentForm


class TestPaymentForm(TestCase):
    def setUp(self):
        product = Product.objects.create(name='Foo', price=100)
        amount = product.price
        payment = Payment(order_amount=amount)
        payment.save()
        order = Order(
            product=product,
            payment=payment,
            count=1,
            amount=amount)
        order.save()
        self.product = product
        self.payment = payment
        self.order = order
        self.form = PaymentForm(instance=payment)

    def test_initial_data(self):
        self.assertEqual(self.form.fields['sum'].initial, self.payment.order_amount)
        self.assertEqual(self.form.fields['paymentType'].initial, self.payment.payment_type)
        self.assertEqual(self.form.fields['customerNumber'].initial, self.payment.customer_number)
        self.assertEqual(self.form.fields['orderNumber'].initial, self.payment.order_number)

    @override_settings(DEBUG=False)
    def test_display_field_names(self):
        display_field_names = ['paymentType', 'cps_email', 'cps_phone']
        for field in self.form.fields:
            if field not in display_field_names:
                self.assertIsInstance(self.form.fields[field].widget, forms.HiddenInput)
