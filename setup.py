from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="myow",
    packages=['self_supervised'],
    install_requires=required)

