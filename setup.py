from setuptools import setup

setup(
    name='excl',
    version='0.1.0',
    py_modules=['excl'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'excl = excl:cli',
        ],
    },
)