# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='edc-export',
    version='0.1.2',
    author=u'BHP Software Engineering & Data Management Center',
    author_email='se-dmc@bhp.org.bw',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/botswana-harvard/edc-export',
    license='GPL license, see LICENSE',
    description='Base models, forms and admin for participant locator in the Edc.',
    long_description=README,
    zip_safe=False,
    keywords='django edc export',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
