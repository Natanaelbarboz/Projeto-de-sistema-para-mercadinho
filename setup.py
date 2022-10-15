from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Projeto de sistema para mercadinho",
    version="0.1.3",
    author="Natanael Barboza",
    author_email="natanaelblima4@gmail.com",
    description="Projeto de sistema para mercadinho",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Natanaelbarboz/Projeto-de-sistema-para-mercadinho.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)