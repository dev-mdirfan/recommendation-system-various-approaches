# Content Based Recommendation System using Flask

from flask import Flask, request, jsonify, render_template, redirect, url_for
from recommend2 import *
app = Flask(__name__)

@app.route('/')
def index2():
    data = pd.read_csv('static/data/recommendData2.csv')
    tables = data.to_html(classes='product_name')
    return render_template('index2.html', data={'tables':tables, 'query':''})

@app.route('/<query>/', methods=['GET', 'POST'])
def predict(query):
    if request.method == 'GET':
        query = request.args.get('query')
        df = Recommend(query)
        df = pd.DataFrame(df.data, columns=['product_name'])
        tables = df.to_html(classes='product_name')
        return render_template('index2.html', data={'tables':tables, 'query':query})
    # data = request.get_json(force=True)
    # return jsonify(data)
    return redirect(url_for('index2'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

