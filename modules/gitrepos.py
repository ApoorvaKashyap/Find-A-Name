import requests


def githubRepos(projectName):
    base_url = "https://api.github.com/search/repositories?"
    query = "q={}&sort=stars&order=desc".format(projectName)
    url = base_url + query
    jsonResponse = requests.get(url)
    return jsonResponse.content


def gitlabRepos(projectName):
    # base_url = "https://gitlab.com"
    pass


def bitbucketRepos(projectName):
    pass
