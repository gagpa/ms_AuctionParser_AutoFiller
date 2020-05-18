from setuptools import setup, find_packages

requirements = [line.strip() for line in open('requirements.txt').readlines()]
packages = find_packages()
setup(name='ms_AutoFiller',
      version='1.0',
      author='oFry',
      packages=packages,
      data_files=['activate.py'],
      install_requires=requirements,
      )
