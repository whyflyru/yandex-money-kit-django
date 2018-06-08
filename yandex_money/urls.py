# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import NoticeFormView
from .views import CheckOrderFormView


urlpatterns = [
    url(r'^check/$', CheckOrderFormView.as_view(), name='yandex_money_check'),
    url(r'^aviso/$', NoticeFormView.as_view(), name='yandex_money_notice'),
]
