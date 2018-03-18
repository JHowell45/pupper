"""
Create setup file for creating package and installing it.

This file is used for adding and creating the application to the specified
python package location.
"""
from os.path import abspath, dirname

from setuptools import find_packages, setup

here = abspath(dirname(__file__))

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='puppo',  # Required
    version='0.1.0',  # Required
    description=('Scripts and commands for running tasks to make your python '
                 'experience easier.'),  # Required
    author='Jacob Howell',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='python commands scripts',
    py_modules=['puppo'],  # Optional
    install_requires=[
        'click',
        'tqdm',
        'twine',
    ],
    entry_points='''
        [console_scripts]
        puppo=__init__:cli
    ''',
    )
