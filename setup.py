import os
import sys

from setuptools import setup, find_packages, Command

here = os.path.abspath(os.path.dirname(__file__))


requires = [
    'pyramid'
    , 'pyramid_mako'
    , 'gevent'
    , 'gevent-socketio'
    , 'pyramid_socketio'
    , 'redis'
]


setup(name='neshack_socketio',
      version='0.0',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = neshack_socketio:main
      """,
      paster_plugins=['pyramid'],
      )
