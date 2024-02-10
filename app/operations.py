from fastapi import HTTPException
from app.modules.gitRepos import githubRepos
from app.modules.langRepos import cppReference, pypi, rubyGems, npm
from app.modules.osRepos import debianRepos,aurRepos, launchpadRepos
from app.models import FinalResponse

async def search(projectName: str) -> FinalResponse:
    response = FinalResponse(projectName=projectName)
    try:
        response.githubRepos = githubRepos(projectName)
        response.cppReference = cppReference(projectName)
        response.pypi = pypi(projectName)
        response.rubyGems = rubyGems(projectName)
        response.npm = npm(projectName)
        response.debianRepos = debianRepos(projectName)
        response.aurRepos = aurRepos(projectName)
        response.launchpadRepos = launchpadRepos(projectName)
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = "Failed to fetch results from the server."
        )
    return response