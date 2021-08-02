import requests
import gitlab


def githubRepos(projectName) -> dict:
    base_url = "https://api.github.com/search/repositories?"
    query = "q={}&sort=stars&order=desc".format(projectName)
    url = base_url + query
    jsonResponse = requests.get(url)
    return jsonResponse.content


def gitlabRepos(projectName):
    gl = gitlab.Gitlab("https://gitlab.com/")
    gl.search("")


def bitbucketRepos(projectName):
    pass


if __name__ == "__main__":
    githubRepos("Audacium")
