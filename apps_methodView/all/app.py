"""
This module is provide recommendation system for e-commerce website.
"""

try:
    from flask import Flask, render_template, request, jsonify, redirect, url_for
    from autocomplete import SearchBar
    from conentBased import Recommend
except Exception as e:
    print("Some Modules are Missing {}".format(e))
    print("Please install the required modules")

app = Flask(__name__)

templates = [
    "pages/index.html",
    "pages/search_results.html",
    "recommend/contentBased.html",
    "recommend/collaborativeFiltering.html",
    "recommend/hybridModels.html",
]

@app.route("/")
def index():
    return render_template(templates[0], context = context)


@app.route("/search_result", methods=["GET"])
def search_result():
    if request.method == "GET":
        # Get the query from the user
        query = request.args.get("query")
        # print(query)
        # Get the results from the query
        obj = SearchBar()
        results = obj.get_results(query)
        # Render the results
        context = {
            "results": results,
        }
        return render_template(templates[1], context = context)
    else:
        context = {
            "results": "No results found",
        }
    return render_template(templates[0], context = context)

# app route for content based recommendation system page
@app.route('/contentBased')
def contentBased():
    contentQuery = request.args.get('contentQuery')
    context['contentQuery'] = contentQuery
    if request.args.get('contentQuery') :
        data, tables = obj2.get_recommendations(contentQuery)
        context['tables'] = tables
        context['data'] = data
        return render_template(templates[2], context = context)
    return render_template(templates[2], context = context)

# app route for collaborative filtering system page
@app.route('/collaborativeFiltering', methods=['GET', 'POST'])
def collaborativeFiltering():
    if request.method == 'GET':
        return render_template(templates[2])
    return redirect(url_for(templates[0]))


if __name__ == "__main__":
    obj1 = SearchBar()
    obj2 = Recommend()
    suggestSearch = obj1.get_suggestions()
    # print(suggestSearch[:5])
    suggestContent = obj2.get_product_name()
    # print(suggestContent[:5])
    context = {
        "suggestSearch": suggestSearch,
        "suggestContent": suggestContent,
    }
    app.run(debug=True)
