import requests
from bs4 import BeautifulSoup as bs


def pypi(projectName):
    base = "https://pypi.org/pypi/"
    endpoint = "/json/"
    url = base + projectName + endpoint
    rawResponse = requests.get(url)
    if "404" not in str(rawResponse):
        # response = rawResponse.json()
        return 0
    else:
        return 1


def npm(projectName):
    base = "https://registry.npmjs.org/-/v1/search?text="
    options = "&size=2"
    url = base + projectName + options
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response["total"] == 0:
        return 1
    else:
        return 0


def rubyGems(projectName):
    base = "https://rubygems.org/api/v1/search.json?query="
    url = base + projectName
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response:
        return 0
    else:
        return 1


def cppReference(projectName):
    projectName = projectName.lower()
    base = "https://en.cppreference.com/w/cpp/links/libs"
    rawResponse = requests.get(base)
    soup = bs(rawResponse.content, "html.parser")
    libs = []
    for lib in soup.find_all("a", {"class": "external text"}):
        libs.append(lib.text.strip().lower())
    if projectName in libs:
        return 0
    else:
        return 1


if __name__ == "__main__":
    res = cppReference("libVLC")
    print(res)
