# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default=b'http://localhost:8000/oplata/fail/', verbose_name='URL \u043d\u0435\u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default=None, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0432\u0438\u0442\u0440\u0438\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default=None, verbose_name='ID \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default=b'http://localhost:8000/oplata/success/', verbose_name='URL \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u044b'),
        ),
    ]
