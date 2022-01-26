from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
DATA_PATH = os.getenv('IMDB_DATA_PATH')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def do_args_allow_row(row, args):
    return all([row[arg] == arg_value for  arg, arg_value in args.items()])

@app.route('/search', methods=['GET'])
def search():
    res = []
    args = request.args

    with open(DATA_PATH, encoding="utf8") as csv_file:
        data = csv.DictReader(csv_file)
        res = [row for row in data if do_args_allow_row(row, args)]

    # id, title, release_date, overview, popularity, vote_average, vote_count, video
    return jsonify(res)
