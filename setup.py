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
    packages=["wevbox"],
    entry_points={"console_scripts": ["wevbox=wevbox.__main__:wevbox"]},
    include_package_data=True
)
