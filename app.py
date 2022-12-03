from flask import Flask, render_template, request
from models.get_data import GetData

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    data = GetData()

    name = data.username
    score = data.scores
    date = data.dates
    length = len(name)
        
    return render_template('list.html', length=length, data=data, name=name, score=score, date=date)

@app.route("/profile", methods=['GET'])
def player_profile():
    data = GetData()
    name = data.username
    score = data.scores
    date = data.dates
    player_name = request.args.get('name')
    player_score = request.args.get('score')
    player_date = request.args.get('date')

    return render_template("profile.html", player_score=player_score, player_date=player_date, name=name, score=score, date=date, player_name=player_name)


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=3000)
