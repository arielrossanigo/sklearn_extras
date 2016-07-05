# coding: utf-8
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


base_path = os.path.dirname(os.path.abspath(__file__))
long_description = open(os.path.join(base_path, 'README.rst')).read()

setup(
    name="sklearn_extras",
    version="0.1.1",
    description="Some extra stuffs that I always use",
    long_description=long_description,
    author="Ariel Rossanigo",
    author_email="arielrossanigo@gmail.com",
    url="https://github.com/arielrossanigo/sklearn_extras",
    packages=[
        "sklearn_extras"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=[
        "machine learning", "scikit", "scikit-learn", "sklearn",
    ],
)
