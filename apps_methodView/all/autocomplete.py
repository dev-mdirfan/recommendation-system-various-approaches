"""
Search bar autocomplete using the product categories
from (product_category_tree) column of the dataset (col=1)
And match with the original dataset (col=15)
"""

try:
    import pandas as pd
    from flask import (
        Flask,
        request,
        jsonify,
        render_template,
        redirect,
        url_for,
        jsonify,
    )
except Exception as e:
    print("Some Modules are Missing {}".format(e))
    print("Suggestion: pip install pandas flask")


class SearchBar:
    """
    Search bar autocomplete using the product categories
    """

    def __init__(self, data=""):
        self.data = data

    def match_query(self, query):
        data = pd.read_csv(
            "static/data/flipkart_com-ecommerce_sample.csv",
            na_values=["No rating available"],
        )
        # Using Apply to search for substring in all dataframe columns
        results = data[
            data.apply(
                lambda row: row.astype(str).str.contains(query, case=False).any(),
                axis=1,
            )
        ]
        # above logic returns all the products
        return results

    def get_results(self, query):
        results = self.match_query(query)
        results = results.to_html(classes="data", header="true")
        return results

    def get_suggestions(self):
        data = pd.read_csv(
            "static/data/autocomplete.csv", na_values=["No rating available"]
        )
        return list(data["product_category_tree"])
        # to json
        # return data["product_category_tree"].str.capitalize().to_json(orient="records")
