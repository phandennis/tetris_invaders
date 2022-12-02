from flask import Flask, render_template, request
import json
import operator

app = Flask(__name__)

@app.route("/")
def home():
    data = 0
    with open('./data/scores.json') as json_file:
        data = json.load(json_file)
        data.sort(key=operator.itemgetter("score"), reverse=True)
    return render_template('list.html', data=data)

@app.route("/sort_by_date")
def sort_by_username():
    data = 0
    with open('./data/scores.json') as json_file:
        data = json.load(json_file)
        data.sort(key=operator.itemgetter("date"), reverse=True)
    return render_template('list.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=3000)
