from flask import Flask, request, jsonify, Response
import csv
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
DATA_PATH = os.getenv('IMDB_DATA_PATH')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def does_arg_allow_row(row, arg):
    arg_key, arg_value = arg
    if arg_key == 'overview':
        # naive implementation
        overview = row[arg_key].lower()
        return any([word in overview for word in arg_value.split(' ')])
    else:
        return row[arg_key].lower() == arg_value.lower()

def do_args_allow_row(row, args):
    return all([does_arg_allow_row(row, arg) for arg in args.items()])

@app.route('/search', methods=['GET'])
def search():
    res = []
    args = request.args

    with open(DATA_PATH, encoding="utf8") as csv_file:
        data = csv.DictReader(csv_file)
        try:
            res = [row for row in data if do_args_allow_row(row, args)]
        except:
            return Response("Filter not found", status=400)

    # todo sort by similarity score in overview

    # id, title, release_date, overview, popularity, vote_average, vote_count, video
    return jsonify(res)
