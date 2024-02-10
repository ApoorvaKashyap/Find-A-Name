import requests
from bs4 import BeautifulSoup as bs


def pypi(projectName) -> bool:
    base = "https://pypi.org/pypi/"
    endpoint = "/json/"
    url = base + projectName + endpoint
    rawResponse = requests.get(url)
    if "404" not in str(rawResponse):
        # response = rawResponse.json()
        return False
    else:
        return True


def npm(projectName) -> bool:
    base = "https://registry.npmjs.org/-/v1/search?text="
    options = "&size=2"
    url = base + projectName + options
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response["total"] == 0:
        return True
    else:
        return False


def rubyGems(projectName) -> bool:
    base = "https://rubygems.org/api/v1/search.json?query="
    url = base + projectName
    rawResponse = requests.get(url)
    response = rawResponse.json()
    if response:
        return False
    else:
        return True


def cppReference(projectName) -> bool:
    projectName = projectName.lower()
    base = "https://en.cppreference.com/w/cpp/links/libs"
    rawResponse = requests.get(base)
    soup = bs(rawResponse.content, "html.parser")
    libs = []
    for lib in soup.find_all("a", {"class": "external text"}):
        libs.append(lib.text.strip().lower())
    if projectName in libs:
        return False
    else:
        return True


if __name__ == "__main__":
    res = cppReference("libVLC")
    print(res)