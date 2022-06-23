# Standard Library
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.0.4"

if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hardik-test",
    version=version,
    description="A simple apple wallet pass generator",
    long_description=long_description,  # Long description read from the readme file
    long_description_content_type="text/markdown",
    author="hardik",
    author_email="harik@primedigital.tech",
    url="https://github.com/hardik-pdgt/Testing-github-actions",
    packages=[
        "src",
    ],
    install_requires=[
        "cryptography",
    ],
    include_package_data=True,
    license="MIT License",
    zip_safe=False,
    keywords="apple wallet pass card",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
