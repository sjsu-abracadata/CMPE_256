from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def text_blob_sentiment(given_sentence):
    overall_results = TextBlob(given_sentence).sentiment
    results = {
        'sentiment': overall_results.polarity,
        'confidence': overall_results.subjectivity
    }
    return results


def vader_sentiment(given_sentence):
    analyser = SentimentIntensityAnalyzer()
    overall_results = analyser.polarity_scores(given_sentence)
    return overall_results

