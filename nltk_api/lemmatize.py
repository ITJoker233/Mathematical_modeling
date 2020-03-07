import nltk,json

def anylyz(sentence):
    VerbNum = AdjNum = NounNum = AdvNum = 0
    VerbWords = AdjWords = NounWords = AdvWords = []
    for word, tag in nltk.pos_tag(nltk.word_tokenize(sentence)):
        if tag.startswith('NN'):
            NounNum += 1
            NounWords.append(word)
        elif tag.startswith('VB'):
            VerbNum += 1
            VerbWords.append(word)
        elif tag.startswith('JJ'):
            AdjNum += 1
            AdjWords.append(word)
        elif tag.startswith('R'):
            AdvNum += 1
            AdvWords.append(word)
        else:
            pass
    result = {
        'Verb':VerbNum,
        'Adjective':AdjNum,
        'Noun':NounNum,
        'Adverb':AdvNum,
        'WorldList':{'Noun':NounWords,'Verb':VerbWords,'Adjective':AdjWords,'Adverb':AdjWords}
    }
    return json.dumps(result)