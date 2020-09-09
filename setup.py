# -*- coding: utf-8 -*-

from pyworxcloud import *
import setuptools

requirements = ['paho-mqtt==1.5.0',
                'pyOpenSSL==17.5.0']

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
