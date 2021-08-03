from flask import Flask, redirect, request

from modules.gitRepos import githubRepos
from modules.langRepos import cppReference, npm, pypi, rubyGems
from modules.osrepos import aurRepos, debianRepos, launchpadRepos

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/ospnc-v2/api/v1/", code=302)


@app.errorhandler(404)
def notFound(e):
    try:
        with open("./html/404.html") as content:
            return content.read()
    except Exception as error:
        return str(error)


@app.route("/ospnc-v2/api/v1/", methods=["GET"])
def hello():
    try:
        with open("./html/content.html") as content:
            return content.read()
    except Exception as e:
        return str(e)


# Code Hosting Websites
@app.route("/ospnc-v2/api/v1/github", methods=["GET"])
def githubAvail():
    if "name" in request.args:
        response = githubRepos(str(request.args["name"]))
        return str(response)


# Language Libraries
@app.route("/ospnc-v2/api/v1/pypi", methods=["GET"])
def pypiAvail():
    if "name" in request.args:
        response = pypi(str(request.args["name"]))
        return str(response)


@app.route("/ospnc-v2/api/v1/npm", methods=["GET"])
def npmAvail():
    if "name" in request.args:
        response = npm(str(request.args["name"]))
        return str(response)


@app.route("/ospnc-v2/api/v1/rubygems", methods=["GET"])
def rubygemsAvail():
    if "name" in request.args:
        response = rubyGems(str(request.args["name"]))
        return str(response)


@app.route("/ospnc-v2/api/v1/cpp", methods=["GET"])
def cppAvail():
    if "name" in request.args:
        response = cppReference(str(request.args["name"]))
        return str(response)


# OS Repos
@app.route("/ospnc-v2/api/v1/debian", methods=["GET"])
def debianAvail():
    if "name" in request.args:
        response = debianRepos(str(request.args["name"]))
        return str(response)


@app.route("/ospnc-v2/api/v1/aur", methods=["GET"])
def aurAvail():
    if "name" in request.args:
        response = aurRepos(str(request.args["name"]))
        return str(response)


@app.route("/ospnc-v2/api/v1/launchpad", methods=["GET"])
def launchpadAvail():
    if "name" in request.args:
        response = launchpadRepos(str(request.args["name"]))
        return str(response)
