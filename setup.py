#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: setup.py
@time: 23/05/2018 12:43
"""

from setuptools import setup, find_packages
from sponge import __version__


setup(
    name='sponge',
    version=__version__,
    description=(
        'An elegant cache library for python'
    ),
    long_description=open('README.md').read(),
    author='William Wei',
    author_email='1342247033@qq.com',
    maintainer='William Wei',
    maintainer_email='1342247033@qq.com',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/IamBusy/sponge',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'redis>=2.10.6',
    ]
)