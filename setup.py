from setuptools import setup, find_packages

setup(
    name='regressionz',
    version='1.0.0',
    url='https://github.com/jtreeves/regressions_api',
    license='MIT',
    author='Jackson Reeves',
    author_email='jr@jacksonreeves.com',
    description='Provides users with access to a Python library that generates regressions models',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['Flask']
)