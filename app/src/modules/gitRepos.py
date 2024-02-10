import requests


def githubRepos(projectName) -> bool:
    base_url = "https://api.github.com/search/repositories?"
    query = "q={}&sort=stars&order=desc".format(projectName)
    url = base_url + query
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response["total_count"] == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    githubRepos("Audacium")
