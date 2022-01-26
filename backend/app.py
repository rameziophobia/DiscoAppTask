from flask import Flask, request, jsonify, Response, send_file
import csv
import os
import file_converter

app = Flask(__name__)
app.config.from_pyfile('config.py')
DATA_PATH = os.getenv('IMDB_DATA_PATH')


@app.route("/")
def hello_world():
    return "<p>Server Online!</p>"


def does_arg_allow_row(row, arg):
    # todo remove special characters
    arg_key, arg_value = arg
    if arg_key.endswith('_at_least'):
        key_without_suffix = arg_key[:-len('_at_least')]
        return float(row[key_without_suffix]) >= float(arg_value)

    if arg_key.endswith('_at_most'):
        key_without_suffix = arg_key[:-len('_at_most')]
        return float(row[key_without_suffix]) <= float(arg_value)

    if arg_key == 'overview':
        # naive implementation that needs optimization
        overview = row[arg_key].lower()
        return any([any([word == ov for ov in overview.split(' ')]) for word in arg_value.split(' ')])

    return row[arg_key].lower() == arg_value.lower()


def do_args_allow_row(row, args):
    return all([does_arg_allow_row(row, arg) for arg in args.items()])


def count_total_words_in_ref(ref_words, words):
    return sum([ref in words.split(' ') for ref in ref_words.split(' ')])


@app.route('/search', methods=['GET'])
def search():
    res = []
    args = request.args

    with open(DATA_PATH, encoding="utf8") as csv_file:
        data = csv.DictReader(csv_file)
        try:
            res = [row for row in data if do_args_allow_row(row, args)]
            if 'overview' in args:
                res.sort(key=lambda row: count_total_words_in_ref(
                    row['overview'], args['overview']), reverse=True)
        except:
            return Response("Filter not found", status=400)
    return jsonify(res)


@app.route('/convert', methods=['POST'])
def convert():
    form = request.form
    file = request.files.get('file')
    fileConverter = file_converter.FileConverter(
        form['fromType'], form['toType'])

    try:
        return fileConverter.convert(file)
    except NotImplementedError:
        return Response("This fromType, toType combination is not supported tyet", status=400)
