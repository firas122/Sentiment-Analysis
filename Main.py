import os

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo
import numpy as np
import flask
from flask import request, jsonify

# vars

MONGO_URI = os.environ.get("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is not set")

client = pymongo.MongoClient(MONGO_URI)
db = client.Test

# definitions

sid_obj = SentimentIntensityAnalyzer()


def sentiment_scores(sentence):

    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict['compound'] >= 0.05:
        s = "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        s = "Negative"

    else:
        s = "Neutral"

    return {"negative_score": sentiment_dict['neg'] * 100,
            "positive_score": sentiment_dict['pos'] * 100,
            "neutral_score": sentiment_dict['neu'] * 100,
            "overall_decision": s}


# main

app = flask.Flask(__name__)


@app.route('/do', methods=['GET', 'POST'])
def home():
    if request.method != 'POST':
        return jsonify({"error": "use POST with an 'offer_id' form field"}), 405

    offer_id = request.form.get('offer_id')
    if not offer_id:
        return jsonify({"error": "missing required form field 'offer_id'"}), 400

    revids = list(db.reviewsData.find({"offer_id": offer_id}, {"rev_id": 1, "text": 1}))

    matrixArr = np.array([])
    for review in revids:
        sent = sentiment_scores(review["text"])
        matrixArr = np.append(matrixArr, [{"review": review["text"], "sentiment_object": sent}])

    return jsonify(matrixArr.tolist())


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host='0.0.0.0', port=3000, debug=debug_mode)
