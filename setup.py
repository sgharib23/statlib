import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statlib",
    version="0.0.1",
    author="dis09",
    author_email="malte.bonart@th-koeln.de",
    description="usefull functions for doing statistics in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dis09/statlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)



