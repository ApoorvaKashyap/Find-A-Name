from mimetypes import init
from typing import Optional
from xmlrpc.client import boolean

from pydantic import BaseModel


class FinalResponse(BaseModel):
    """
    The class containing the model for the final response that will be parsed and shown in the index.html as results.
    The default is "False" meaning that the name is not available. It will be changed to True within the main function.
    """

    projectName: str
    githubRepos: bool = False
    cppReference: bool = False
    npm: bool = False
    pypi: bool = False
    rubyGems: bool = False
    aurRepos: bool = False
    debianRepos: bool = False
    launchpadRepos: bool = False
