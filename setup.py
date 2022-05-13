# encoding: utf8
from distutils.core import setup
from setuptools import find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['matplotlib']

setup(name='koreanize-matplotlib',
      version='0.0.1',
      description='matplotlib의 폰트 설정을 자동으로 한국어화',
      author='ychoi-kr',
      author_email='ychoi_kr@naever.com',
      url='https://github.com/ychoi-kr/koreanize-matplotlib',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      package_data={
          'koreanize_matplotlib': ['fonts/*'],
      })
