import nltk,json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def clearSen(comment):
    return comment.strip().replace('，', '。').replace('、', '').replace('《', '。').replace('》', '。').replace('～', '').replace('…', '').replace('\r', '').replace('\t', ' ').replace('\f', ' ').replace('/', '').replace('、', ' ').replace('/', '').replace('。', '').replace('（', '').replace('）', '').replace('_', '').replace('?', ' ').replace('？', ' ').replace('了', '').replace('➕', '').replace('：', '')

def clearWord(text):
    return text.replace('button','').replace('microwave','').replace('door','').replace('kitchen','').replace('Amazon','').replace('<br/>','').replace('<br>','').replace('br','').replace('model','')#.replace('model','')

def anylyz(sentence):
    VerbNum = AdjNum = NounNum = AdvNum = 0
    VerbWords = AdjWords = NounWords = AdvWords = []
    raw_words = nltk.word_tokenize(clearWord(sentence))
    # 词形归一化
    wordnet_lematizer = WordNetLemmatizer()
    words = [wordnet_lematizer.lemmatize(raw_word) for raw_word in raw_words]
    # 去除停用词
    filtered_words = ','.join([word for word in words if word not in stopwords.words('english')])
    for word, tag in nltk.pos_tag(nltk.word_tokenize(filtered_words)):
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
        'WordList':{'Noun':NounWords,'Verb':VerbWords,'Adjective':AdjWords,'Adverb':AdvWords}
    }
    return json.dumps(result)