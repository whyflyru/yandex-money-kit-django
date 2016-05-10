# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import Signal

payment_process = Signal()
payment_completed = Signal()