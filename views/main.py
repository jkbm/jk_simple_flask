
from flask import render_template, Blueprint


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    return "Hello, world!"


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")