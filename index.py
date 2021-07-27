from flask import Flask, request
from modules.gitrepos import githubRepos

app = Flask(__name__)


@app.route("/ospnc-v2/api/v1/", methods=["GET"])
def hello():
    return """
    <h1> Welcome to OSPNC v2 </h1>
    <h4> Developed by <a href="https://github.com/ApoorvaKashyap">Apoorva Kashyap</a></h4>
    <hr>
    These are the current active repository lists that OSPNC checks in for available project names.
    <ol>
    <li>Github (<a href="https://github.com">https://github.com</a>)</li>
    <li>In progress...</li>
    </ol>
    """


@app.route("/ospnc-v2/api/v1/github", methods=["GET"])
def gitAvail():
    if "name" in request.args:
        response = githubRepos(str(request.args["name"]))
        return response
