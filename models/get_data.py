import json
import operator

class GetData:
    """
    This is used to read the the json file, and then write into the json file
    """

    def __init__(self):
        self.filename = ('./data/scores.json')
        self.username = []
        self.scores = []
        self.dates = []
        self.load_json_file()

    def load_json_file(self):
        with open(self.filename, "r") as json_file:
            self.data = json.load(json_file)

            self.data.sort(key=operator.itemgetter("score"), reverse=True)

        for player_name in self.data:
            self.username.append(player_name['username'])

        for scores in self.data:
            self.scores.append(scores['score'])

        for date in self.data:
            self.dates.append(date['date'])

