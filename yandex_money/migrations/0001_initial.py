# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import yandex_money.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('shop_id', models.PositiveIntegerField(default=1, verbose_name='ID \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430')),
                ('scid', models.PositiveIntegerField(default=0, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0432\u0438\u0442\u0440\u0438\u043d\u044b')),
                ('customer_number', models.CharField(default=yandex_money.utils.get_formatted_uuid, max_length=64, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430')),
                ('order_amount', models.DecimalField(verbose_name='\u0421\u0443\u043c\u043c\u0430 \u0437\u0430\u043a\u0430\u0437\u0430', max_digits=15, decimal_places=2)),
                ('article_id', models.PositiveIntegerField(null=True, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0442\u043e\u0432\u0430\u0440\u0430', blank=True)),
                ('payment_type', models.CharField(default=b'PC', max_length=2, verbose_name='\u0421\u043f\u043e\u0441\u043e\u0431 \u043f\u043b\u0430\u0442\u0435\u0436\u0430', choices=[(b'PC', '\u041a\u043e\u0448\u0435\u043b\u0435\u043a \u042f\u043d\u0434\u0435\u043a\u0441.\u0414\u0435\u043d\u044c\u0433\u0438'), (b'AC', '\u0411\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u0430\u044f \u043a\u0430\u0440\u0442\u0430'), (b'GP', '\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u0447\u0435\u0440\u0435\u0437 \u043a\u0430\u0441\u0441\u044b \u0438 \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u044b'), (b'MC', '\u0421\u0447\u0435\u0442 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'), (b'WM', '\u041a\u043e\u0448\u0435\u043b\u0435\u043a WebMoney'), (b'SB', '\u0421\u0431\u0435\u0440\u0431\u0430\u043d\u043a: \u043e\u043f\u043b\u0430\u0442\u0430 \u043f\u043e SMS \u0438\u043b\u0438 \u0421\u0431\u0435\u0440\u0431\u0430\u043d\u043a \u041e\u043d\u043b\u0430\u0439\u043d'), (b'AB', '\u0410\u043b\u044c\u0444\u0430-\u041a\u043b\u0438\u043a'), (b'MA', 'MasterPass'), (b'PB', '\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442-\u0431\u0430\u043d\u043a \u041f\u0440\u043e\u043c\u0441\u0432\u044f\u0437\u044c\u0431\u0430\u043d\u043a\u0430'), (b'QW', 'QIWI Wallet'), (b'QP', '\u0414\u043e\u0432\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u043b\u0430\u0442\u0435\u0436 (\u041a\u0443\u043f\u043f\u0438.\u0440\u0443)')])),
                ('order_number', models.CharField(default=yandex_money.utils.get_formatted_uuid, max_length=64, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430')),
                ('cps_email', models.EmailField(max_length=100, null=True, verbose_name='Email \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430', blank=True)),
                ('cps_phone', models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a\u0430', blank=True)),
                ('success_url', models.URLField(default=b'https://example.com/success-payment/', verbose_name='URL \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u044b')),
                ('fail_url', models.URLField(default=b'https://example.com/fail-payment/', verbose_name='URL \u043d\u0435\u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u044b')),
                ('status', models.CharField(default=b'processed', max_length=16, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(b'processed', b'Processed'), (b'success', b'Success'), (b'fail', b'Fail')])),
                ('invoice_id', models.PositiveIntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430', blank=True)),
                ('shop_amount', models.DecimalField(decimal_places=2, max_digits=15, blank=True, help_text='\u0417\u0430 \u0432\u044b\u0447\u0435\u0442\u043e\u043c \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430', null=True, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u0430\u044f \u043d\u0430 \u0440/\u0441')),
                ('order_currency', models.PositiveIntegerField(default=643, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430', choices=[(643, '\u0420\u0443\u0431\u043b\u0438'), (10643, '\u0422\u0435\u0441\u0442\u043e\u0432\u0430\u044f \u0432\u0430\u043b\u044e\u0442\u0430')])),
                ('shop_currency', models.PositiveIntegerField(default=643, null=True, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u0430\u044f \u043d\u0430 \u0440/\u0441', blank=True, choices=[(643, '\u0420\u0443\u0431\u043b\u0438'), (10643, '\u0422\u0435\u0441\u0442\u043e\u0432\u0430\u044f \u0432\u0430\u043b\u044e\u0442\u0430')])),
                ('performed_datetime', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u0430', blank=True)),
                ('user', models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': '\u043f\u043b\u0430\u0442\u0451\u0436',
                'verbose_name_plural': '\u043f\u043b\u0430\u0442\u0435\u0436\u0438',
            },
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together=set([('shop_id', 'order_number')]),
        ),
    ]