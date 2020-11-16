from setuptools import setup


dependencies = ["pytest", "pytest-cov"]


setup(
    name="data_structures_pkg",
    description="Data structures",
    package_dir={"": "src"},
    install_requires=dependencies
)