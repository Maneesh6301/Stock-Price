from setuptools import find_packages,setup
from typing import List
Hyphen="-e ."

def requirements(file_path:str)->List[str]:
    """
    This function reads requirements file

    """
    requirements=[]
    with open("requirements.txt") as file_obj:
        requirements=file_obj.readlines()
    requirements=[req.strip() for req in requirements if req.strip()]
    print(requirements)
    requirements=[req for  req in requirements if req!=Hyphen]
    print(requirements)
    return requirements

setup(
    name="Stock Price",
    version="0.0.0.1",
    author="maneesh",
    author_email="maneesh6301@gmail.com",
    packages=find_packages(),
    install_requires=requirements("requirements.txt")
)