# -*- coding: utf-8 -*-

import os
from distutils.core import setup
from setuptools import find_packages

__author__ = 'Yandex.Money'
__version__ = '1.1.0'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-yandex-money',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/yandex-money/yandex-money-kit-django',
    license='MIT',
    author=__author__,
    author_email='cms@yamoney.ru',
    keywords=['django', 'yandex', 'money', 'payment', 'pay'],
    description='Integrating django project with yandex-money',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.4',
        'South>=0.7.5',
        'lxml>=2.3.4',
    ],
)
