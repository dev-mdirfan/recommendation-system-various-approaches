'''
Autocomplete the search bar with the product categories
from (product_category_tree) column of the dataset (col=1).
'''


import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for, jsonify
app = Flask(__name__)

def get_suggestions():
    data = pd.read_csv("static/data/autocomplete.csv", na_values=["No rating available"])
    return list(data['product_category_tree'].str.capitalize())


@app.route("/")
def index():
    suggestions = get_suggestions()
    return render_template('autocomplete2.html', suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)


