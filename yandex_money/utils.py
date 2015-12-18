# -*- coding: utf-8 -*-
from uuid import uuid4


def get_formatted_uuid():
    return str(uuid4()).replace('-', '')
