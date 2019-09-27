from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'requests>=2.22.0'
]

setup(
    name='dcimglib',
    version='0.0.1',
    long_description=long_description,
    url='https://github.com/riemannulus/dcimglib',
    author='Lee, Suho',
    author_email='suho.love@hitagi.moe',
    license='MIT',
    packages=find_packages(),
    install_requires=requires,
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    package_dir={'dcimglib': 'dcimglib'},
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='DCinside'
)
