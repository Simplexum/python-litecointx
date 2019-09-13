#!/usr/bin/env python

from setuptools import setup, find_packages
import os

from litecointx import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = ['python-bitcointx>=1.0.0,<2']

setup(name='python-litecointx',
      version=__version__,
      description='Litecoin module for use with python-bitcointx',
      long_description=README,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
      ],
      python_requires='>=3.6',
      url='https://github.com/Simplexum/python-litecointx',
      keywords='litecoin',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      test_suite="litecointx.tests"
      )
