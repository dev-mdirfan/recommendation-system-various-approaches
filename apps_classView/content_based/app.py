"""
This module is class based recommendation system for e-commerce website.
"""

from flask import Flask, render_template, request, jsonify, redirect, jsonify
from flask.views import View

app = Flask(__name__)


class Home(View):
    def __init__(self, data, template):
        self.data = data
        self.template = template
    
    def index(self):
        return render_template(self.template)


home =  view_func = Home.as_view("data", Home, "pages/index.html")
app.add_url_rule("/", view_func=home)
