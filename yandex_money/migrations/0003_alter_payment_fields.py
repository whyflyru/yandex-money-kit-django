# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import yandex_money.models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0002_auto_20151214_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_number',
            field=models.CharField(default=yandex_money.models.get_random_string, verbose_name='Идентификатор плательщика', max_length=64),
        ),
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default=settings.YANDEX_MONEY_FAIL_URL, verbose_name='URL неуспешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.CharField(default=yandex_money.models.get_random_string, verbose_name='Номер заказа', max_length=64),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(default='PC', verbose_name='Способ платежа', choices=[('PC', 'Кошелек Яндекс.Деньги'), ('AC', 'Банковская карта'), ('GP', 'Наличными через кассы и терминалы'), ('MC', 'Счет мобильного телефона'), ('WM', 'Кошелек WebMoney'), ('SB', 'Сбербанк: оплата по SMS или Сбербанк Онлайн'), ('AB', 'Альфа-Клик'), ('MA', 'MasterPass'), ('PB', 'Интернет-банк Промсвязьбанка'), ('QW', 'QIWI Wallet'), ('QP', 'Доверительный платеж (Куппи.ру)')], max_length=2),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default=settings.YANDEX_MONEY_SCID, verbose_name='Номер витрины'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default=settings.YANDEX_MONEY_SHOP_ID, verbose_name='ID магазина'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='processed', verbose_name='Статус', choices=[('processed', 'Processed'), ('success', 'Success'), ('fail', 'Fail')], max_length=16),
        ),
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default=settings.YANDEX_MONEY_SUCCESS_URL, verbose_name='URL успешной оплаты'),
        ),
    ]
