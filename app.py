import operator
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

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=3000)
