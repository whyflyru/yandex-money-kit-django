# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import NoticeFormView
from .views import CheckOrderFormView


urlpatterns = patterns('',
    url(r'^check/', CheckOrderFormView.as_view(), name='yandex_money_check'),
    url(r'^aviso/', NoticeFormView.as_view(), name='yandex_money_notice'),
)
