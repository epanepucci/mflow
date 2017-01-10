#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='mflow',
      version='0.0.13',
      description='Utility library for ZMQ data streaming',
      author='Paul Scherrer Institute',
      license='GNU GPLv3',
      packages=['mflow', 'mflow.utils', 'mflow.handlers'],
      install_requires=[
          'pyzmq',
      ],
     )
