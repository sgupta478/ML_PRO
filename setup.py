### Will be able to deploy ML project as a Package 

from setuptools import find_packages , setup
from typing import List
hypen = "-e . "
def get_requirements(file_path: str) -> List[str]:
    " This function will return the list of Req."

    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n" , " ") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)

        return requirements


setup(
name = "ML_PRO",
version = '0.0.1' , 
author = "SIDDHANT" ,
author_email= "sgupta47@buffalo.edu",
packages= find_packages() ,
install_requires = get_requirements('requirements.txt') ,



)