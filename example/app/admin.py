# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Goods
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('goods', 'count', 'payment', 'amount')
    list_filter = ('goods', )

admin.site.register(Goods)
admin.site.register(Order, OrderAdmin)