"""
This module is provide recommendation system for e-commerce website.
"""

try:
    from flask import Flask, render_template, request, jsonify, redirect, url_for
    from autocomplete import SearchBar
    from conentBased import Recommend
    from collaborative import Collaborative
except Exception as e:
    print("Some Modules are Missing {}".format(e))
    print("Please install the required modules")

app = Flask(__name__)

templates = [
    "pages/index.html",
    "pages/search_results.html",
    "recommend/contentBased.html",
    "recommend/collaborative.html",
    "recommend/hybrid.html",
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
@app.route('/collaborative', methods=['GET', 'POST'])
def collaborative():
    collaborativeQuery = request.args.get('collaborativeQuery')
    context['collaborativeQuery'] = collaborativeQuery
    if request.args.get('collaborativeQuery') :
        data, tables = obj3.get_recommendations(collaborativeQuery)
        context['tables'] = tables
        context['data'] = data
        return render_template(templates[3], context = context)
    return render_template(templates[3], context = context)


if __name__ == "__main__":
    obj1 = SearchBar()
    suggestSearch = obj1.get_suggestions()
    # print(suggestSearch[:5])
    obj2 = Recommend()
    suggestContent = obj2.get_product_name()
    # print(suggestContent[:5])
    obj3 = Collaborative()
    suggestCollaborative = obj3.get_product_id()
    # print(suggestCollaborative[:5])
    context = {
        "suggestSearch": suggestSearch,
        "suggestContent": suggestContent,
        "suggestCollaborative": suggestCollaborative,
    }
    app.run(debug=True)
