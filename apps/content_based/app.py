# Content Based Recommendation System using Flask

from flask import Flask, request, jsonify, render_template, redirect, url_for
from recommend import *
app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('static/data/recommendData.csv')
    tables = data.to_html(classes='product_name')
    return render_template('index.html', data={'tables':tables})

@app.route('/<query>/', methods=['GET', 'POST'])
def predict(query):
    if request.method == 'GET':
        query = request.args.get('query')
        df = recommend(query)
        tables = df.to_html(classes='data')
        return render_template('index.html', data={'tables':tables})
    # data = request.get_json(force=True)
    # return jsonify(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

