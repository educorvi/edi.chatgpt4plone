# -*- coding: utf-8 -*-
"""Installer for the edi.chatgpt4plone package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.md').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='edi.chatgpt4plone',
    version='1.0a1',
    description="A ChatGPT Integration for Plone-Search based on LangChain Framework",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT",
    ],
    keywords='Python Plone',
    author='Lars Walther und Julian Pollinger',
    author_email='info@educorvi.de',
    url='https://github.com/collective/edi.chatgpt4plone',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/edi.chatgpt4plone',
        'Source': 'https://github.com/collective/edi.chatgpt4plone',
        'Tracker': 'https://github.com/collective/edi.chatgpt4plone/issues',
        # 'Documentation': 'https://edi.chatgpt4plone.readthedocs.io/en/latest/',
    },
    license='MIT',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['edi'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
        'websockets',
        'langchain~=0.0.169',
        'openai~=0.27.2',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = edi.chatgpt4plone.locales.update:update_locale
    """,
)
