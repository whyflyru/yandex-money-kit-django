from __future__ import unicode_literals
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',

    'yandex_money',
    'tests'
]

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE_CLASSES = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

SECRET_KEY = 'asd'

# Required in Django 1.9
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'}]

YANDEX_MONEY_SCID = 123
YANDEX_MONEY_SHOP_ID = 456
YANDEX_MONEY_SHOP_PASSWORD = 'password'
YANDEX_MONEY_DEBUG = DEBUG
YANDEX_MONEY_FAIL_URL = 'http://example.com/fail-payment/'
YANDEX_MONEY_SUCCESS_URL = 'http://example.com/success-payment/'
