#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='email-sender',
    version='0.0.3',
    author='cielpy',
    author_email='wutongci@gmail.com',
    url='https://github.com/wutongci/email-sender',
    description='发邮件',
    packages=find_packages(),
    install_requires=['sender'],
)