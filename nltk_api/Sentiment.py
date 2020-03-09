import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def anylyz(sentences): # If the score is greater than 0, we're happy. Otherwise it is not happy
    senti = SentimentIntensityAnalyzer()
    result = dict()
    result['sum'] = 0.0
    for sentence in sentences:
        sentence = str(sentence)
        sentence = sentence.replace('"',"'")
        kvp = senti.polarity_scores(sentence)
        result[sentence] = kvp['compound']
        result['sum'] += kvp['compound']
    return result