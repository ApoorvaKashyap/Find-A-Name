from app.src.models import FinalResponse
from app.src.modules.gitRepos import githubRepos
from app.src.modules.langRepos import cppReference, npm, pypi, rubyGems
from app.src.modules.osRepos import aurRepos, debianRepos, launchpadRepos
from fastapi import HTTPException


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
            status_code=500, detail="Failed to fetch results from the server."
        )
    return response
