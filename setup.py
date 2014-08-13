import os
import re

from setuptools import setup, find_packages


MODULE_NAME = 'dyntftpd'

DEPENDENCIES = []
TEST_DEPENDENCIES = []


def find_file(*paths):
    return os.path.join(os.path.dirname(__file__), *paths)


def get_version():
    """ Reads package version number from package's __init__.py. """
    with open(find_file(MODULE_NAME, '__init__.py')) as init:
        for line in init.readlines():
            res = re.match(r'^__version__ = [\'"](.*)[\'"]$', line)
            if res:
                return res.group(1)

        raise NotImplementedError(
            '%s does not have a __version__ defined in '
            '__init__.py' % MODULE_NAME
        )


def get_long_description():
    """ Reads description from README and CHANGES. """
    with open(find_file('README.md')) as readme, \
        open(find_file('CHANGES.md')) as changes:
        return readme.read() + '\n' + changes.read()


setup(
    name=MODULE_NAME,
    version=get_version(),
    description='A simple TFTP server',
    long_description=get_long_description(),
    author='Julien Castets',
    author_email='castets.j@gmail.com',
    url='https://github.com/brmzkw/dyntftpd',
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    tests_require=DEPENDENCIES + TEST_DEPENDENCIES,
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2 :: Only',  # fuck python3
        'Topic :: Internet :: File Transfer Protocol (FTP)'
    ],
    entry_points={
        'console_scripts': [
            'dyntftpd = dyntftpd.cli:main'
        ]
    }
)
