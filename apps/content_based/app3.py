# Content Based Recommendation System using Flask

from flask import Flask, request, jsonify, render_template, redirect, url_for, jsonify
from recommend3 import *
app = Flask(__name__)

@app.route('/')
def index3():
    data1 = pd.read_csv('static/data/recommendData3.csv')
    # product_name = data['product_name']
    data2 = df.original_data
    # Merging data together
    data = pd.merge(data1, data2, on='product_name', how='inner')
    data.to_json('./static/data/recommendData3.json')
    # jsonify(data)
    # combine data into tuple to show it to user
    tables = [data.to_html(classes='product_name')]
    # titles = data.columns.values
    data = data.to_dict('records')
    data = [tuple(x.values()) for x in data]
    return render_template('index3.html', exp = {'data':data, 'tables':tables, 'query':''})

@app.route('/<query>/', methods=['GET', 'POST'])
def predict(query):
    if request.method == 'GET':
        query = request.args.get('query')
        # query = request.form['query']
        df = Recommend(query)
        data1 = df.data
        data2 = df.original_data
        # Merging data together
        data = pd.merge(data1, data2, on='product_name', how='inner')
        # product_specification = data['product_specification']
        tables = [data.to_html(classes='product_name')]
        # titles=data.columns.values
        # Combine data into tuple to show it to user
        data = data.to_dict('records')
        data = [tuple(x.values()) for x in data]
        return render_template('index3.html', exp = {'data':data, 'tables':tables, 'query':query})
    # data = request.get_json(force=True)
    # return jsonify(data)
    return redirect(url_for('index3'))

if __name__ == '__main__':
    df = Recommend()
    app.run(port=5000, debug=True)

