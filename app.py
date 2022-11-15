from flask import Flask, request, jsonify, make_response, abort
from werkzeug.exceptions import HTTPException

import functions
import model
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def find_keywords(data):
    if data is None:
        return jsonify({"error": "No data provided"})
    paragraph = data['text']
    if paragraph == '' or len(paragraph) == 0:
        return jsonify({"error": "No text provided"})
    keywords = model.get_keywords(paragraph)
    if len(keywords) == 0:
        abort(400, "No keywords found! Try Again…")
    return keywords


@app.route('/keywords', methods=["POST"])
@cross_origin()
def get_keywords():
    return jsonify(find_keywords(request.json))


@app.route('/sound', methods=["POST"])
@cross_origin()
def get_sound():
    response = functions.get_audio(find_keywords(request.json), only_one=True)
    if response is None:
        abort(400, "No audio found!")
    return jsonify(response)


@app.route('/sounds', methods=["POST"])
@cross_origin()
def get_sounds():
    response = functions.get_audio(find_keywords(request.json), only_one=False)
    if response is None:
        abort(400, "No audio found!")
    return jsonify(response)


@app.route('/grammar', methods=["POST"])
@cross_origin()
def grammar():
    data = request.json
    text = data['text']
    return jsonify(model.check_grammar(text))


@app.route('/report', methods=["POST"])
@cross_origin()
def report():
    data = request.json
    word = data['text']
    return jsonify(functions.report(word))


@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.description}), e.code


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)
