from setuptools import setup, find_packages
from typing import List

# Constant for the editable flag
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of dependencies.
    It excludes the '-e .' entry used for local package installation.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            # Remove newlines
            requirements = [req.replace("\n", "") for req in requirements]
            
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
        
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Lakshay',
    author_email='lakshaynaharwal7@gmail.com',
    description='A comprehensive Machine Learning pipeline project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)