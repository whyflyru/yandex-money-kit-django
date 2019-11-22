# Generated by Django 2.2.7 on 2019-11-22 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0005_auto_20191107_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default='http://example.com/fail-payment/', verbose_name='URL неуспешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default=123, verbose_name='Номер витрины'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default=456, verbose_name='ID магазина'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default='http://example.com/success-payment/', verbose_name='URL успешной оплаты'),
        ),
    ]