from distutils.core import setup

setup(
  name = 'jinja-tools',
  version = '0.1a',
  description = (
    'various tools for Jinja2'
    ' including new filters and tests based on python-moretools'
    ' and a simple jinja2 based JinjaBuilder class for scons'
    ),

  author = 'Stefan Zimmermann',
  author_email = 'zimmermann.code@googlemail.com',
  url = 'http://bitbucket.org/StefanZimmermann/jinja-tools',

  license = 'LGPLv3',

  packages = ['jinjatools.scons'],

  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved ::'
    ' GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development',
    'Topic :: Utilities',
    ],

  keywords = [
    'jinja', 'jinja2', 'tools', 'template', 'macro',
    'filter', 'test', 'moretools', 'builder', 'build',
    ],
  )
