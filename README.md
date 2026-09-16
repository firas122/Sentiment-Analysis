# Sentiment-Analysis

A small Flask API that runs [VADER](https://github.com/cjhutto/vaderSentiment) sentiment
analysis over customer reviews stored in MongoDB for a given offer, and returns a
per-review sentiment breakdown.

## What it does

For a given `offer_id`, the API pulls all matching documents from the `reviewsData`
collection (each expected to have a `text` field), runs VADER sentiment scoring on
each review's text, and returns the reviews together with their sentiment scores.

## Setup

```bash
pip install -r requirements.txt
```

Set the MongoDB connection string as an environment variable before running:

```bash
export MONGO_URI="mongodb+srv://<user>:<password>@<cluster>/<db>"
```

## Run

```bash
python Main.py
```

The server listens on `http://0.0.0.0:3000`.

## Usage

`POST /do` with a form field `offer_id`:

```bash
curl -X POST http://localhost:3000/do -d "offer_id=<some-offer-id>"
```

Example response:

```json
[
  {
    "review": "Great product, fast shipping!",
    "sentiment_object": {
      "negative_score": 0.0,
      "positive_score": 65.2,
      "neutral_score": 34.8,
      "overall_decision": "Positive"
    }
  }
]
```

`GET /do` and requests missing `offer_id` return a `4xx` JSON error instead of a result.

## License

MIT — see [LICENSE](LICENSE).
