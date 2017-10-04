# coding: utf-8

"""
    SNC API

    This is an API server for the data scraped from the SNC website.

    OpenAPI spec version: 1.0.0
    Contact: not-an-email@example.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SNC API",
    author_email="not-an-email@example.org",
    url="",
    keywords=["Swagger", "SNC API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is an API server for the data scraped from the SNC website.
    """
)