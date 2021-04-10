# -*- coding:utf-8 -*-
import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="MedView",
    version="0.0.1",
    author="timothy",
    author_email="thyzyfx@qq.com",
    description="3d show tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimothyZero/Medical-Image-Visualization",
    packages=['medview'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)