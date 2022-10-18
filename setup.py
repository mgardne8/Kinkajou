""" Run `pip install -e .` from the root directory to install Kinkajou from this project
"""
from setuptools import find_packages, setup

setup(
    name="Kinkajou",
    version="0.0.1.localdev",
    author="Matt Gardner",
    author_email="Matt@M-Gardner.info",
    url="https://github.com/mgardne8/Kinkajou",
    description="Kinkajou Is Not Kinkajou, Amazingly Just Outright Useless. A ripoff data library.",
    license="MIT",
    packages=find_packages(),
)
