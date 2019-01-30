#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='hiii-email-sender',
    version='0.0.3',
    author='cielpy',
    author_email='beijiu572@gmail.com',
    url='https://github.com/cielpy/hiii-email-sender',
    description='hiii 发邮件',
    packages=find_packages(),
    install_requires=['sender'],
)