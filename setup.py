try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Describe the project',
    'author': 'Kushal Khandelwal',
    'url': 'URL of the project',
    'download_url': 'Download URL',
    'author_email': 'kushal124@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['MODULE'],
    'scripts': [],
    'name': 'projec tname',
    'license': ''
	
}

setup(**config)
