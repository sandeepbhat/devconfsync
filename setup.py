# MIT License

# Copyright (c) 2020 Sandeep Bhat

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Setup tool configuration."""

import setuptools

PACKAGE_NAME = "devconfsync"
PACKAGE_VERSION = "0.0.1"

LONG_DESCRIPTION = ""
DEPENDENCIES = list()

with open("requirements.txt") as requirements:
    for req in requirements:
        DEPENDENCIES.append(req)

with open("README.md") as readme:
    LONG_DESCRIPTION = readme.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Development settings sync",
    author="Sandeep Bhat",
    author_email="sandeep.anand.bhat@gmail.com",
    license="MIT License",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/sandeepbhat/devconfsync",
    packages=["devconfsync"],
    install_requires=DEPENDENCIES,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"
    ]
)
