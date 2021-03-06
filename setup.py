#coding: utf-8

from setuptools import setup, find_packages

import pelican_admin

setup(
    name='pelican_admin',
    version=pelican_admin.__VERSION__,
    author='Flávio Caetano',
    author_email='flavio@vieiracaetano.com',
    packages=find_packages(),
    url='https://github.com/fjcaetano/pelican_admin',
    license='GPL - see LICENSE.txt',
    description='Django admin app for Pelican blogs.',
    long_description=open('PYREADME.md').read(),
    install_requires=[
        "psutil >= 0.6.1",
        "Django >= 1.4",
        "pelican >= 3.0",
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    platforms='any',
    zip_safe=False,
)