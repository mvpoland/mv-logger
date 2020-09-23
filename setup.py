from setuptools import setup, find_packages


install_requires = [
    "python-logstash-async==2.0.0",
]


setup(
    name="mv-logger",
    version="1.0.1",
    license="MIT",
    author_email="kontakt@mobilevikings.pl",
    author="Mobile Vikings PL",
    description="mv-logger",
    url="https://github.com/mv-poland/mv-logger",
    long_description=open("README.md", "r").read(),
    packages=find_packages("."),
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3 :: 3.5",
        "Programming Language :: Python :: 3 :: 3.6",
        "Programming Language :: Python :: 3 :: 3.7",
        "Programming Language :: Python :: 3 :: 3.8",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
    ],
    python_requires=">=3.5",
)
