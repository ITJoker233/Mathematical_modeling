import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def anylyz(sentences): # If the score is greater than 0, we're happy. Otherwise it is not happy
    senti = SentimentIntensityAnalyzer()
    result = dict()
    for sentence in sentences:
        kvp = senti.polarity_scores(sentence)
        result[sentence] = kvp['compound']
    return result
