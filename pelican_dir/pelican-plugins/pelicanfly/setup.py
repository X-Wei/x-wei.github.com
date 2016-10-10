from setuptools import setup

def readme():
    with open('README') as f:
        return f.read()

setup(name='pelicanfly',
      version='0.4.2',
      description='Font Awesome from inside a Pelican',
      long_description=readme(),
      url='http://bmcorser.github.com/pelicanfly',
      author='bmcorser',
      author_email='benmarshallcorser@gmail.com',
      license='GPL',
      include_package_data=True,
      packages=['pelicanfly'],
      package_dir={'pelicanfly': 'pelicanfly'},
      package_data={'pelicanfly': ['static/css/*', 'static/fonts/*']},
      install_requires=['pelican', 'fontawesome_markdown'],
      zip_safe=False,
      )
