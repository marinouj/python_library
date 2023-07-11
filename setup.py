from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='testpackage',
    version='0.0.1',    
    description='A simple Python package.',
    url='',
    author='Ioanna Marinou',
    author_email='marinoujoanna@gmail.com',
    license='MIT',
    packages=['testpackage'],
    install_requires=required,
    package_data={'': ['data/*.txt']},
    include_package_data=True,
)