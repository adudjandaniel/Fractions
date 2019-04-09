from distutils.core import setup

config = {
    'description': 'My Fraction Data Structure',
    'author': 'Daniel Adu-Djan',
    'url': '',
    'download_url': '',
    'author_email': 'adudjan.danieladd@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'package_dir': {'': 'lib'},
    'packages': ['fraction'],
    'scripts': [],
    'name': 'Fraction'
}

setup(**config)