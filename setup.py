from distutils.core import setup

from setuptools import find_packages, setup

long_description = u'\n\n'.join((
    open('README.rst').read(),
))

setup(
  name = 'toxtest',
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'tox test',   # Give a short description about your library
  long_description=long_description,
  author = 'cuneyt',                   # Type in your name
  author_email = 'cuneyt@3bfab.com',      # Type in your E-Mail
  url = 'https://github.com/3bfab/pipenv-update-check',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/3bfab/pipenv-update-check/archive/refs/tags/v_0.2.5.tar.gz',    # I explain this later on
  install_requires=[            # I get to this in a second
          
      ],
  classifiers=[
  ],
  package_dir={"": "src"},
    packages=find_packages(
        where="src",
    ),  
  package_data={},
    include_package_data=True,
    entry_points={'console_scripts': [
        'toxtest= network',
    ]},
)
