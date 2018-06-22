from setuptools import find_packages, setup

setup(name='api4shared',
      version='0.1',
      description='Python API for 4shared.com',
      author='Hugo Laloge',
      author_email='hugo.laloge@gmail.com',
      url='https://github.com/Hugal31/python-api4shared',
      packages=find_packages(exclude=['tests']),
      zip_safe=True,
      install_requires=['requests-oauthlib>=1'])
