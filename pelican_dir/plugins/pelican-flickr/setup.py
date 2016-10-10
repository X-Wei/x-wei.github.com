try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(
  name='pelican-flickr',
  packages=['pelican-flickr', ],
  version='0.1.1',
  author='Bastien Abadie',
  author_email='bastien.abadie@gmail.com',
  url='https://github.com/La0/pelican-flickr',
  license='LICENSE.txt',
  description='Pelican plugin to add Flickr sets and photos to your website.',
  long_description=open('README.rst').read(),
  install_requires=[
    "flickrapi >= 1.4.2",
  ],
)
