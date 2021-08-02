import requests


def githubRepos(projectName) -> dict:
    base_url = "https://api.github.com/search/repositories?"
    query = "q={}&sort=stars&order=desc".format(projectName)
    url = base_url + query
    jsonResponse = requests.get(url)
    return jsonResponse.content


def gitlabRepos(projectName):
    pass


if __name__ == "__main__":
    githubRepos("Audacium")
