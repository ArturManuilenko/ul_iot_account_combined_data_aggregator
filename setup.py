from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='data-aggregator-sdk',
    version='2.2.21',
    description='Data aggregator sdk',
    author='Unic-lab',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='a.brilon@unic-lab.by',
    url='git@gitlab.neroelectronics.by:unic-lab/projects/iot_account/ul_iot_account_combined_data_aggregator.git',
    package_data={'': ['*.yml'], },
    packages=find_packages(include=['data_aggregator_sdk*']),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    platforms='any',
    install_requires=[
        'requests>=2.26.0',
        'unipipeline>=1.4.3'
    ]
)
