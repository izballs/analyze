from flask import Flask, request
import json
import collections

app = Flask(__name__)


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

if __name__ == "__main__":
        app.run(host="0.0.0.0", port="80")
