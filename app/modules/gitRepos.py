import requests


def githubRepos(projectName) -> dict:
    base_url = "https://api.github.com/search/repositories?"
    query = "q={}&sort=stars&order=desc".format(projectName)
    url = base_url + query
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response["total_count"] == 0:
        return 1
    else:
        return 0


def gitlabRepos(projectName):
    pass


if __name__ == "__main__":
    githubRepos("Audacium")
