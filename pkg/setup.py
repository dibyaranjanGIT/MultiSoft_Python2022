from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="packagedibya",
    version="0.0.1",
    author="dibya",
    author_email="dibya@gmail.com",
    packages=["packagedibya"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/dibyaranjanGIT/test-tackage",
    license='MIT',
    install_requires=[]
)
