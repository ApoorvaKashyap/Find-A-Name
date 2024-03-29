import requests
from bs4 import BeautifulSoup as bs


def debianRepos(projectName) -> bool:
    base = "https://packages.debian.org/search?keywords="
    add_args = "&searchon=names&exact=1&suite=all&section=all"
    url = base + projectName.lower() + add_args
    rawResponse = requests.get(url)
    soup = bs(rawResponse.content, "html.parser")
    div = soup.find("div", {"id": "psearchres"})
    tag = div.find("strong")
    try:
        int(tag.text)
        print(tag.text)
    except Exception as e:
        print(e)
        return True
    else:
        return False


def aurRepos(projectName) -> bool:
    base = "https://aur.archlinux.org/packages/?O=0&SeB=N&K="
    add_args = "&outdated=&SB=n&SO=a&PP=50&do_Search=Go"
    url = base + projectName.lower() + add_args
    rawResponse = requests.get(url)
    soup = bs(rawResponse.content, "html.parser")
    if soup.find("tbody") is None:
        return True
    else:
        return False


def launchpadRepos(projectName) -> bool:
    base = "https://api.launchpad.net/1.0/"
    url = base + projectName.lower()
    rawResponse = requests.get(url)
    if rawResponse.status_code == 404:
        return True
    else:
        return False


if __name__ == "__main__":
    res = launchpadRepos("dfh")
    print(res)
