from setuptools import setup, find_packages

install_requires = [
    'python-logstash-async==2.0.0',
]


setup(
    name="mv-logger",
    version='1.0.0',
    license='MIT',
    author_email='kontakt@mobilevikings.pl',
    author='Mobile Vikings PL',
    description='mv-logger',
    url='https://github.com/mv-poland/mv-logger',
    long_description=open('README.md', 'r').read(),
    packages=find_packages('.'),
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
    ],
)
