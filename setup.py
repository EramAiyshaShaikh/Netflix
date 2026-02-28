from setuptools import setup,find_packages
from typing import List

hyphen='-e .'
def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file:
        requirement=file.readlines()
        requirement=[req.replace('/n','') for req in requirement]

        if hyphen in requirement:
            requirement.remove(hyphen)  

    return requirement        

setup(
    name='Netflix',
    version='0.0.1',
    author='Eram',
    author_email='eram.s1994@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)