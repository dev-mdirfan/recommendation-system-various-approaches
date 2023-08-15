'''
Autocomplete Search Bar (product_name) column used of the main dataset (cols=15)

'''

import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for, jsonify
app = Flask(__name__)

# pre_df = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])

# product_category_tree = pre_df["product_category_tree"]
# description = pre_df["description"]
# product_specifications = pre_df["product_specifications"]
# product_name = pre_df["product_name"]


# print(product_category_tree.head(5)[0])
# print(description.head(5))
# print(product_specifications.head(5))
# print(product_name.head(5))

def get_suggestions():
    data = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
    return list(data['product_name'].str.capitalize())


@app.route("/")
def index():
    suggestions = get_suggestions()
    return render_template('autocomplete.html', suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)


