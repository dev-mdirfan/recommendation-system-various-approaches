"""
This module is provide recommendation system for e-commerce website.
"""

try:
    from flask import Flask, render_template, request, jsonify, redirect, url_for
    from autocomplete import SearchBar
    from conentBased import Recommend
    from collaborative import Collaborative
    from hybrid import Hybrid
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
    "pages/about.html",
]

@app.route("/")
def index():
    return render_template(templates[0], context = context)

@app.route("/about")
def about():
    return render_template(templates[5], context = context)


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
        context['results'] = results
        return render_template(templates[1], context = context)
    else:
        context['results'] = "No results found"
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
        data, tables = obj3.get_recommendations(str(collaborativeQuery))
        context['tables'] = tables
        context['data'] = data
        return render_template(templates[3], context = context)
    return render_template(templates[3], context = context)

@app.route('/hybrid', methods=['GET', 'POST'])
def hybrid():
    hybridQuery1 = request.args.get('hybridQuery1')
    hybridQuery2 = request.args.get('hybridQuery2')
    if request.args.get('hybridQuery') or request.args.get('hybridQuery2') :
        data = obj4.get_recommendations(hybridQuery1, hybridQuery2)
        context['data'] = data
        context['hybridQuery1'] = hybridQuery1
        context['hybridQuery2'] = hybridQuery2
        return render_template(templates[4], context = context)
    return render_template(templates[4], context = context)

if __name__ == "__main__":
    obj1 = SearchBar()
    suggestSearch = obj1.get_suggestions()
    # print(suggestSearch[:5])
    obj2 = Recommend()
    suggestContent = obj2.get_product_name()
    columnNamesCB = obj2.get_column_names()
    # print(suggestContent[:5])
    obj3 = Collaborative()
    suggestCollaborative = obj3.get_product_id()
    columnNamesCF = obj3.get_column_names()
    # print(suggestCollaborative[:5])
    obj4 = Hybrid()
    suggestHybrid1 = obj4.get_user_id()
    suggestHybrid2 = obj4.get_product_id()
    context = {
        "suggestSearch": suggestSearch,
        "suggestContent": suggestContent,
        "suggestCollaborative": suggestCollaborative,
        "suggestHybrid1": suggestHybrid1,
        "suggestHybrid2": suggestHybrid2,
        "columnNamesCB": columnNamesCB,
        "columnNamesCF": columnNamesCF,
    }
    app.run(debug=True)
