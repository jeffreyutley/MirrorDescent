from setuptools import setup, find_packages, Extension
import numpy as np
import os

NAME = "MirrorDescent"
VERSION = "0.1"
DESCR = 'An implementation of Mirror Descent from Chapter 9 of ``First-Order Methods in Optimization`` by Amir Beck'
REQUIRES = ['numpy']
LICENSE = "BSD-3-Clause"

AUTHOR = 'MirrorDescent development team'
EMAIL = "buzzard@purdue.edu"
PACKAGE_DIR = "MirrorDescent"

setup(install_requires=REQUIRES,
      zip_safe=False,
      name=NAME,
      version=VERSION,
      description=DESCR,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      packages=find_packages(include=['MirrorDescent']),
      )

