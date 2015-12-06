#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='jeff',
    version='0.2.0',
    description='Jeff generates license file from the command line.',
    author='Oskar Cieslik',
    author_email='oskar.cieslik@gmail.com',
    url='https://github.com/oskarcieslik/Jeff',
    download_url='https://github.com/oskarcieslik/Jeff',
    keywords=['license', 'github', 'python', 'command line', 'cli'],
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'docopt>=0.6.2',
    ],
    package_data={
        'jeff': ['licenses/*']
    },
    entry_points={
        'console_scripts': [
            'jeff=jeff.jeff:main'
        ],
    }
)
