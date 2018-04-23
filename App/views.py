import random

from flask import Blueprint, render_template, request

from App.ext import db

blue = Blueprint("blue", __name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)
