from setuptools import setup

VERSION = '0.0.1'

def readme():
    with open("README.md") as file:
        return file.read()

setup(
    name="wevbox",
    version=VERSION,
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="development local php",
    url="https://github.com/danilocgsilva/wevbox",
    author="Danilo Silva",
    author_email="contato@danilocgsilva.me",
    package=["src"],
    entry_points={"console_scripts": ["wevbox==src.__main__:main"]},
    include_package_data=True
)
