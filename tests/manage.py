#!/usr/bin/env python
# vim:fileencoding=utf-8
import os
import sys

from django.core.management import execute_from_command_line


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, str(PROJECT_PATH))
    execute_from_command_line(sys.argv)
