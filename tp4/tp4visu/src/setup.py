__author__="Morgan Bidois <morgan.bidois@e.ujf-grenoble.fr>"
__date__ ="$19 nov. 2013 10:20:23$"

from setuptools import setup,find_packages

setup (
  name = 'tp4visu',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Morgan Bidois <morgan.bidois@e.ujf-grenoble.fr>',
  author_email = '',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)