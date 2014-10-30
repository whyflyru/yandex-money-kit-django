# -*- coding: utf-8 -*-

from uuid import uuid4

from django.conf import settings
from django.db import models

from .signals import payment_process
from .signals import payment_completed


class Payment(models.Model):
    class STATUS:
        PROCESSED = 'processed'
        SUCCESS = 'success'
        FAIL = 'fail'

        CHOICES = (
            (PROCESSED, 'Processed'),
            (SUCCESS, 'Success'),
            (FAIL, 'Fail'),
        )

    class PAYMENT_TYPE:
        PC = 'pc'
        AC = 'ac'
        GP = 'gp'
        MC = 'mc'
        WM = 'wm'
        SB = 'sb'
        AB = 'ab'

        CHOICES = (
            (PC, 'Яндекс.Деньги'),
            (AC, 'Банковская карта'),
            (GP, 'По коду через терминал'),
            (MC, 'Со счета мобильного телефона'),
            (WM, 'WebMoney'),
            (SB, 'Выставление счета в Сбербанк.Онлайн'),
            (AB, 'Выставление счета в АльфаКлик'),
        )

    class CURRENCY:
        RUB = 643
        TEST = 10643

        CHOICES = (
            (RUB, 'Рубли'),
            (TEST, 'Тестовая валюта'),
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True,
        verbose_name='Пользователь')
    pub_date = models.DateTimeField('Время создания', auto_now_add=True)

    # Required request fields
    shop_id = models.PositiveIntegerField(
        'ID магазина', default=settings.YANDEX_MONEY_SHOP_ID)
    scid = models.PositiveIntegerField(
        'Номер витрины', default=settings.YANDEX_MONEY_SCID)
    customer_number = models.CharField(
        'Идентификатор плательщика', max_length=64,
        default=lambda: str(uuid4()).replace('-', ''))
    order_amount = models.DecimalField(
        'Сумма заказа', max_digits=15, decimal_places=2)

    # Non-required fields
    article_id = models.PositiveIntegerField(
        'Идентификатор товара', blank=True, null=True)
    payment_type = models.CharField(
        'Способ платежа', max_length=2, default=PAYMENT_TYPE.PC,
        choices=PAYMENT_TYPE.CHOICES)
    order_number = models.CharField(
        'Номер заказа', max_length=64,
        default=lambda: str(uuid4()).replace('-', ''))
    cps_email = models.EmailField(
        'Email плательщика', max_length=100, blank=True, null=True)
    cps_phone = models.CharField(
        'Телефон плательщика', max_length=15, blank=True, null=True)
    success_url = models.URLField(
        'URL успешной оплаты', default=settings.YANDEX_MONEY_SUCCESS_URL)
    fail_url = models.URLField(
        'URL неуспешной оплаты', default=settings.YANDEX_MONEY_FAIL_URL)

    # Transaction info
    status = models.CharField(
        'Статус', max_length=16, choices=STATUS.CHOICES,
        default=STATUS.PROCESSED)
    invoice_id = models.PositiveIntegerField(
        'Номер транзакции оператора', blank=True, null=True)
    shop_amount = models.DecimalField(
        'Сумма полученная на р/с', max_digits=15, decimal_places=2, blank=True,
        null=True, help_text='За вычетом процента оператора')
    order_currency = models.PositiveIntegerField(
        'Валюта', default=CURRENCY.RUB, choices=CURRENCY.CHOICES)
    shop_currency = models.PositiveIntegerField(
        'Валюта полученная на р/с', blank=True, null=True,
        default=CURRENCY.RUB, choices=CURRENCY.CHOICES)
    performed_datetime = models.DateTimeField(
        'Время выполнение запроса', blank=True, null=True)

    @property
    def is_payed(self):
        return self.status == self.STATUS.SUCCESS

    def send_signals(self):
        status = self.status
        if status == self.STATUS.PROCESSED:
            payment_process.send(sender=self)
        if status == self.STATUS.SUCCESS:
            payment_completed.send(sender=self)

    class Meta:
        ordering = ('-pub_date',)
        unique_together = (
            ('shop_id', 'order_number'),
        )
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
