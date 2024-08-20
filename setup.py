# setup.py
from setuptools import setup, find_packages

setup(
    name="ZenoPay",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    description="A Python package for interacting with the Zeno Africa API",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/ZenoPay",
)
