from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    """
    Reads a requirements file and returns a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    # Remove any comments and empty lines
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)   
    return requirements

setup(    name='mlproject1',
    version='0.0.1',author='Sairam',author_email='sairam.qd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A simple machine learning project')
# setup(    name='mlproject1',
#     version='0.0.1',author='Sairam',author_email='sairam.qd@gmail.com',
#     packages=find_packages(),
#     install_requires=['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn'],
#     description='A simple machine learning project')