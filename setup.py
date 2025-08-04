from setuptools import setup, find_packages
from typing import List


def get_requirements()->list[str]:
   
   requirements : List[str] = []
   
   return requirements

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Adil",
    author_email = "madilshahzad6@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)