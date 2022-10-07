import json

from flask import Flask, redirect, request, render_template
from flask_cors import CORS
from app.modules.gitRepos import githubRepos
from app.modules.langRepos import cppReference, npm, pypi, rubyGems
from app.modules.osrepos import aurRepos, debianRepos, launchpadRepos

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    title = "Find-A-Name"
    return render_template('index.html', title=title)


@app.errorhandler(404)
def notFound(e):
    return render_template('404.html', title="Page Not Found")


@app.route("/find-a-name/api/v1/", methods=["GET"])
def hello():
    return render_template('content.html', title="Endpoint Base")


# Code Hosting Websites
@app.route("/find-a-name/api/v1/github", methods=["GET"])
def githubAvail():
    if "name" in request.args:
        response = githubRepos(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "Github Endpoint"
        )


# Language Libraries
@app.route("/find-a-name/api/v1/pypi", methods=["GET"])
def pypiAvail():
    if "name" in request.args:
        response = pypi(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "PyPi Endpoint"
        )


@app.route("/find-a-name/api/v1/npm", methods=["GET"])
def npmAvail():
    if "name" in request.args:
        response = npm(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "NPM Endpoint"
        )


@app.route("/find-a-name/api/v1/rubygems", methods=["GET"])
def rubygemsAvail():
    if "name" in request.args:
        response = rubyGems(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "RubyGems Endpoint"
        )


@app.route("/find-a-name/api/v1/cpp", methods=["GET"])
def cppAvail():
    if "name" in request.args:
        response = cppReference(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "CPP Endpoint"
        )


# OS Repos
@app.route("/find-a-name/api/v1/debian", methods=["GET"])
def debianAvail():
    if "name" in request.args:
        response = debianRepos(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "Debian Endpoint"
        )


@app.route("/find-a-name/api/v1/aur", methods=["GET"])
def aurAvail():
    if "name" in request.args:
        response = aurRepos(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "AUR Endpoint"
        )


@app.route("/find-a-name/api/v1/launchpad", methods=["GET"])
def launchpadAvail():
    if "name" in request.args:
        response = launchpadRepos(str(request.args["name"]))
        return str(response)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "LaunchPad Endpoint"
        )


# Give back a consolidated result
@app.route("/find-a-name/api/v1/all", methods=["GET"])
def allResults():
    response = {}
    jsonResponse = ""
    if "name" in request.args:
        response["github"] = str(githubRepos(str(request.args["name"])))
        response["pypi"] = str(pypi(str(request.args["name"])))
        response["npm"] = str(npm(str(request.args["name"])))
        response["rubyGems"] = str(rubyGems(str(request.args["name"])))
        response["cpp"] = str(cppReference(str(request.args["name"])))
        response["aur"] = str(aurRepos(str(request.args["name"])))
        response["debian"] = str(debianRepos(str(request.args["name"])))
        response["launchpad"] = str(launchpadRepos(str(request.args["name"])))
        jsonResponse = json.dumps(response, indent=4)
    else:
        return """
            <!DOCTYPE html>
            <head>
                <title>{}</title>
            </head>
            <body>
                Please pass the name argument.
            </body>
        """.format(
            "Consolidated Endpoint"
        )
    return jsonResponse
