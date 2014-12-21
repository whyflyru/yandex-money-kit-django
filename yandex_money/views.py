# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings
from django.core.mail import mail_admins
from lxml import etree
from lxml.builder import E

from .forms import CheckForm
from .forms import NoticeForm
from .models import Payment


logger = logging.getLogger('yandex_money')


class YandexValidationError(Exception):
    params = None

    def __init__(self, params=None):
        super(YandexValidationError, self).__init__()
        self.params = params if params is not None else {}


class BaseView(View):
    form_class = None

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if form.check_md5(cd):
                payment = self.get_payment(cd)
                if payment:
                    try:
                        self.validate(cd, payment)
                    except YandexValidationError as exc:
                        params = exc.params
                    else:
                        params = self.get_response_params(payment, cd)
                        self.mark_payment(payment, cd)
                        payment.send_signals()
                else:
                    params = {'code': '1000'}
            else:
                params = {'code': '1'}
        else:
            params = {'code': '200'}

        self.logging(request, params)
        content = self.get_xml(params)

        if (
            settings.get('YANDEX_MONEY_MAIL_ADMINS_ON_PAYMENT_ERROR', True) and
            params.get('code') != '0'
        ):
            mail_admins('yandexmoney_django error', u'post data: {post_data}\n\nresponse:{response}'.format(
                post_data=request.POST,
                response=content,
            ))

        return HttpResponse(content, content_type='application/xml')

    def validate(self, data, payment):
        pass

    def get_payment(self, cd):
        try:
            payment = Payment.objects.get(
                order_number=cd['orderNumber'], shop_id=cd['shopId'])
        except Payment.DoesNotExist:
            payment = None
        return payment

    def get_response_params(self, payment, cd):
        if payment:
            now = datetime.now()

            payment.performed_datetime = now
            payment.save()

            return {'code': '0',
                    'shopId': str(cd['shopId']),
                    'invoiceId': str(cd['invoiceId']),
                    'performedDatetime': now.isoformat()}
        return {'code': '100'}

    def mark_payment(self, payment, cd):
        pass

    def get_xml(self, params):
        element = self.get_xml_element(**params)
        return etree.tostring(element,
                              pretty_print=True,
                              xml_declaration=True,
                              encoding='UTF-8')

    def get_xml_element(self, **params):
        raise NotImplementedError()

    def logging(self, request, params):
        message = 'Action %s has code %s for customerNumber "%s"' % (
            request.POST.get('action', ''), params['code'],
            request.POST.get('customerNumber', ''))
        logger.info(message)


class CheckOrderFormView(BaseView):
    form_class = CheckForm

    def validate(self, data, payment):
        if payment.order_amount != data['orderSumAmount']:
            params = {
                'code': '100',
                'message': u'Неверно указана сумма платежа',
            }
            raise YandexValidationError(params=params)

    def get_xml_element(self, **params):
        return E.checkOrderResponse(**params)


class NoticeFormView(BaseView):
    form_class = NoticeForm

    def get_xml_element(self, **params):
        return E.paymentAvisoResponse(**params)

    def mark_payment(self, payment, cd):
        payment.cps_email = cd.get('cps_email', '')
        payment.cps_phone = cd.get('cps_phone', '')
        payment.order_currency = cd.get('orderSumCurrencyPaycash')
        payment.shop_amount = cd.get('shopSumAmount')
        payment.shop_currency = cd.get('shopSumCurrencyPaycash')
        payment.payer_code = cd.get('paymentPayerCode')
        payment.payment_type = cd.get('paymentType')
        payment.status = payment.STATUS.SUCCESS
        payment.save()