# -*- coding: utf-8 -*-

import os
from setuptools import setup


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


__author__ = 'Yandex.Money'
__version__ = '1.4.1+whyfly.3'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_yandex_money',
    version=__version__,
    packages=get_packages('yandex_money'),
    package_data=get_package_data('yandex_money'),
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
