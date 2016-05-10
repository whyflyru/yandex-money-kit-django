# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4


def get_formatted_uuid():
    return str(uuid4()).replace('-', '')
