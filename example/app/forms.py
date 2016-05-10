# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from yandex_money.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('scid', 'shopID', 'CustomerNumber', 'Sum', 'paymentType')