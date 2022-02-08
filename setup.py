# -*- coding: utf-8 -*-

from worxcloud_sc import *
import setuptools

requirements = ['paho-mqtt==1.6.1',
                'pyOpenSSL==21.0.0',
                'ratelimit==2.2.1']


setuptools.setup(
    name = 'worxcloud_sc',
    description = 'Worx Landroid API library',
    author = 'Morten Trab',
    author_email = 'morten@trab.dk',
    license= 'MIT',
    url = 'https://github.com/SCC-github/worxcloud_sc',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
