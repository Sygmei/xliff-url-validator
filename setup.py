# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["xliff_url_validator", "uvicorn"]

package_data = {"": ["*"]}

install_requires = ["fastapi>=0.78.0,<0.79.0"]

setup_kwargs = {
    "name": "xliff-url-validator",
    "version": "0.1.0",
    "description": "",
    "long_description": None,
    "author": "Sygmei",
    "author_email": None,
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.10,<4.0",
}


setup(**setup_kwargs)
