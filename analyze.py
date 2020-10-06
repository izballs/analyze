from flask import Flask, request, Blueprint
import re
import json
import collections


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route("/analyze", methods=["POST"])
def analyze():
        json = request.get_json()
        withLength = len(json['text'])
        withoutLength = len(json['text'].replace(" ", ""))
        wordCount = len(json['text'].split())
        parsedSTR = re.findall("[a-z]", json["text"].lower().replace(" ", ""))
        lettercount = collections.Counter(parsedSTR)
        letterCountHolder = []
        for letter in lettercount.items():
            letterCountHolder.append({letter[0]:letter[1]})
        returnJson = {'textLength': {'withSpaces': withLength, "withoutSpaces":withoutLength}, "wordCount": wordCount, "characterCount":letterCountHolder}
        return returnJson

@app.route('/')
def index():
    return "<h1>Analyze Dream Broker</h1><p>Code Challenge</p>"
