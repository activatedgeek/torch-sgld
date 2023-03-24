import os
from setuptools import setup, find_packages

VERSION = os.environ.get('GITHUB_REF', 'v0.0.0-alpha1')
if VERSION.startswith('refs/tags'):
    VERSION = VERSION.split('/')[-1]

with open('README.md') as f:
    README = f.read()

setup(
    name='torch-sgld',
    description='SGLD as PyTorch Optimizer',
    long_description=README,
    long_description_content_type='text/markdown',
    version=VERSION,
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    packages=find_packages(exclude=[
        'scripts',
        'scripts.*',
        'experiments',
        'experiments.*',
        'notebooks',
        'notebooks.*',
    ]),
    install_requires=['torch'],
    extras_require={})