try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Lexicon project',
    'author': 'Tom Fahner',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tom.fahner@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': 'ex48',
    'scripts': ['lexicon.py'],
    'name': 'Excercise 48'
}

setup(**config)