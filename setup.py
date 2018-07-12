# -*- coding: utf-8 -*-

import os
from distutils.core import setup
from setuptools import find_packages

__author__ = 'Yandex.Money'
__version__ = '1.3.3wf'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_yandex_money',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.10',
        'lxml>=3.3.4',
        'six'
    ],
    test_suite='tests.runtests.runtests',
    test_requires=[
        'coveralls',
        'coverage',
        'django-discover-runner'
    ]
)
