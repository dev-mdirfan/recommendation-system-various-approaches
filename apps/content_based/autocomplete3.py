'''
Autocomplete the search bar with the product categories
from (product_category_tree) column of the dataset (col=1).
'''


import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for, jsonify
app = Flask(__name__)

def match_query(q):
    data = pd.read_csv("static/data/flipkart_com-ecommerce_sample.csv", na_values=["No rating available"])
    # return data[data['product_category_tree'].str.contains(q, case=False)]         # It returns only one product
    # Using Apply to search for substring in all dataframe columns
    results = data[data.apply(lambda row: row.astype(str).str.contains(q, case=False).any(), axis=1)]   # It returns all the products
    return results


def get_suggestions():
    data = pd.read_csv("static/data/autocomplete.csv", na_values=["No rating available"])
    return list(data['product_category_tree'].str.capitalize())


@app.route("/")
def index():
    suggestions = get_suggestions()
    return render_template('autocomplete3.html', suggestions=suggestions)

@app.route("/search_result", methods=["GET"])
def search_result():
    query = request.args.get('query')
    
    results = match_query(str(query))
    # return results.to_json(orient='records')
    tables = results.to_html(classes='data', header="true")
    return render_template('autocomplete3_result.html', tables=tables)

if __name__ == "__main__":
    app.run(debug=True)



