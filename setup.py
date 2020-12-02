# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='wagtail-graphql',
    version='0.2.1',
    description='An app to automatically add GraphQL support to a Wagtail website',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "homepage": "https://github.com/tr11/wagtail-graphql",
        "repository": "https://github.com/tr11/wagtail-graphql"
    },
    author='Tiago Requeijo',
    author_email='tiago.requeijo.dev@gmail.com',
    license='MIT',
    keywords='wagtail graphql api wagtail-graphql',
    packages=['wagtail_graphql', 'wagtail_graphql.types'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'graphene-django==2.*,>=2.2.0',
        'graphene-django-optimizer==0.*,>=0.3.5',
        'python-dateutil==2.*,>=2.6.0', 'wagtail==2.*,>=2.3.0'
    ],
    extras_require={
        "dev": [
            "django-cors-headers==2.*,>=2.4.0", "flake8==3.*,>=3.6.0",
            "mypy>=0.790", "pytest==4.*,>=4.0.0", "pytest-cov==2.*,>=2.6.0",
            "pytest-django==3.*,>=3.4.0", "pytest-flake8==1.*,>=1.0.0",
            "pytest-mypy==0.*,>=0.3.2", "pytest-pythonpath==0.*,>=0.7.3"
        ],
        "menus": ["wagtailmenus==3.*,>=3.0.0"]
    },
)
