from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo as pymongo
import numpy as np
import flask
from flask import request

#vars

client = pymongo.MongoClient("mongo connection string here")
db = client.Test

#definitions

def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)


    if sentiment_dict['compound'] >= 0.05:
        s = "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        s = "Negative"

    else:
        s = "Neutral"

    return({"nagative_score": sentiment_dict['neg'] * 100,
            "positive_score": sentiment_dict['pos'] * 100,
            "neutral_score": sentiment_dict['neu'] * 100,
           "overall_decision": s})

#main


#definitions

app = flask.Flask(__name__)

@app.route('/do', methods=['GET', 'POST'])
def home():
    matrixArr = np.array([])
    if request.method == 'POST':
        p = request.form.get('offer_id')
    revids = db.reviewsData.find({"offer_id": p}, {"rev_id": 1, "text": 1})
    for i in range(db.reviewsData.count_documents({"offer_id": "0026ceed-e2f5-4cf4-a958-2e13e0550564"}) - 1):
        sent = sentiment_scores(revids[i]["text"])
        matrixArr = np.append(matrixArr, [{"review": revids[i]["text"], "sentiment_object": sent}])
    return(matrixArr.tolist())

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=3000, debug=True)
