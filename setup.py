from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='kaedim_package',
    version='0.0.1',    
    description='A simple Python package.',
    url='',
    author='Name Surname',
    author_email='marinoujoanna@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=required,
    package_data={'': ['data/*.txt']},
    include_package_data=True,
)