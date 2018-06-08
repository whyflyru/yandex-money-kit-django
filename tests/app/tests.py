# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hashlib import md5
import xml.etree.ElementTree as ET

from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django import forms
from django.conf import settings

from .models import Product, Order
from yandex_money.models import Payment
from yandex_money.forms import PaymentForm, BasePaymentForm


ACTION_CHECK = 'checkOrder'
ACTION_NOTICE = 'paymentAviso'


class TestBasePaymentForm(TestCase):
    def setUp(self):
        self.form_class = BasePaymentForm()

    def test_md5(self):
        cd = {
            'action': ACTION_CHECK,
            'orderSumAmount': '100',
            'orderSumCurrencyPaycash': '100',
            'orderSumBankPaycash': '123',
            'shopId': settings.YANDEX_MONEY_SHOP_ID,
            'invoiceId': '1',
            'customerNumber': '1'
        }

        hash_string = ';'.join(map(str, (
            cd['action'],
            cd['orderSumAmount'],
            cd['orderSumCurrencyPaycash'],
            cd['orderSumBankPaycash'],
            cd['shopId'],
            cd['invoiceId'],
            cd['customerNumber'],
            settings.YANDEX_MONEY_SHOP_PASSWORD
        )))
        hash_string = hash_string.encode('utf-8')
        md5string = md5(hash_string).hexdigest().upper()
        self.assertEqual(md5string, self.form_class.make_md5(cd))


class BaseTest(TestCase):
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

    def make_md5(self, action=None):
        cd = {
            'action': action,
            'orderSumAmount': '100',
            'orderSumCurrencyPaycash': '100',
            'orderSumBankPaycash': '123',
            'shopId': settings.YANDEX_MONEY_SHOP_ID,
            'invoiceId': '1',
            'customerNumber': '1'
        }
        return self.form.make_md5(cd)


class TestPaymentForm(BaseTest):
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


class TestCheckURL(BaseTest):
    def get_valid_data(self):
        return {
            'requestDatetime': '2011-05-04T20:38:00.000+04:00',
            'action': ACTION_CHECK,
            'md5': self.make_md5(action=ACTION_CHECK),
            'orderNumber': self.payment.order_number,
            'scid': settings.YANDEX_MONEY_SCID,
            'shopId': settings.YANDEX_MONEY_SHOP_ID,
            'invoiceId': '1',
            'shopArticleId': '1',
            'customerNumber': '1',
            'orderCreatedDatetime': '2011-05-04T20:38:00.000+04:00',
            'paymentPayerCode': '42007148320',
            'orderSumAmount': '100',
            'orderSumCurrencyPaycash': '100',
            'orderSumBankPaycash': '123',
            'shopSumAmount': '100',
            'shopSumCurrencyPaycash': '100',
            'shopSumBankPaycash': '100',
            'paymentType': 'AC'
        }

    def test_valid_request(self):
        data = self.get_valid_data()
        response = self.client.post(reverse('yandex_money_check'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '0')

    def test_invalid_md5(self):
        data = self.get_valid_data()
        data['md5'] = 'asd'
        response = self.client.post(reverse('yandex_money_check'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '200')

    def test_invalid_order_number(self):
        data = self.get_valid_data()
        data['orderNumber'] = '123456'
        response = self.client.post(reverse('yandex_money_check'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '1000')

    def test_invalid_data(self):
        data = {}
        response = self.client.post(reverse('yandex_money_check'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '200')


class TestNoticeURL(BaseTest):
    def get_valid_data(self):
        return {
            'requestDatetime': '2011-05-04T20:38:00.000+04:00',
            'action': ACTION_NOTICE,
            'md5': self.make_md5(action=ACTION_NOTICE),
            'orderNumber': self.payment.order_number,
            'scid': settings.YANDEX_MONEY_SCID,
            'shopId': settings.YANDEX_MONEY_SHOP_ID,
            'invoiceId': '1',
            'shopArticleId': '1',
            'customerNumber': '1',
            'orderCreatedDatetime': '2011-05-04T20:38:00.000+04:00',
            'paymentPayerCode': '42007148320',
            'orderSumAmount': '100',
            'orderSumCurrencyPaycash': '100',
            'orderSumBankPaycash': '123',
            'shopSumAmount': '100',
            'shopSumCurrencyPaycash': '100',
            'shopSumBankPaycash': '100',
            'paymentType': 'AC'
        }

    def test_valid_request(self):
        data = self.get_valid_data()
        response = self.client.post(reverse('yandex_money_notice'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '0')

    def test_invalid_md5(self):
        data = self.get_valid_data()
        data['md5'] = 'asd'
        response = self.client.post(reverse('yandex_money_notice'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '200')

    def test_invalid_order_number(self):
        data = self.get_valid_data()
        data['orderNumber'] = '123456'
        response = self.client.post(reverse('yandex_money_notice'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '1000')

    def test_invalid_data(self):
        data = {}
        response = self.client.post(reverse('yandex_money_notice'), data=data)
        el = ET.fromstring(response.content)
        self.assertEqual(el.get('code'), '200')