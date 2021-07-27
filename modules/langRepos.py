import requests


def pypi(projectName):
    base = "https://pypi.org/pypi/"
    endpoint = "/json/"
    url = base + projectName + endpoint
    rawResponse = requests.get(url)
    if '404' not in str(rawResponse):
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


if __name__ == "__main__":
    res = npm("gihk")
    print(res)
