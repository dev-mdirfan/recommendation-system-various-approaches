"""
This module is provide recommendation system for e-commerce website.
"""

try:
    from flask import Flask, render_template, request, jsonify, redirect
    from autocomplete import SearchBar
except Exception as e:
    print("Some Modules are Missing {}".format(e))
    print("Please install the required modules")

app = Flask(__name__)

templates = ['pages/index.html', 'pages/search_results.html', 'pages/autocomplete3_result.html']

@app.route('/')
def index():
    suggestions = SearchBar.get_suggestions()
    context = {
        'suggestions': suggestions,
        }
    return render_template(templates[0], context=context)

@app.route("/search_result", methods=["GET"])
def search_result():
    if request.method == 'GET':
        # Get the query from the user
        query = request.args.get('query')
        # Get the results from the query
        results = SearchBar.get_results(query)
        # Render the results
        context = {
            'results': results,
            }
        return render_template(templates[1], context=context)
    context = {
        'results': 'No results found',
    }
    return render_template(templates[0], context = context)

if __name__ == '__main__':
    app.run(debug=True)

