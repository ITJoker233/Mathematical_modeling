from excel import *
import wordcloud,json
import  nltk_api.Lemmatize as Lemmatize

w = wordcloud.WordCloud(max_words=200,width=800,height=400,margin=5,background_color='white')
filename = '锋利.xlsx'
excel = Excel('SORT_DATA/{0}'.format(filename))
reviews = excel.readColData(13) #列数 从0开始
sentence_list = ''
for item in reviews:
    sentence_list += item + '\n'
json_obj = json.loads(Lemmatize.anylyz(sentence_list))
#result_info = 'Adjective Numbers: {0} \nVerb Numbers: {1} \nNoun Numbers: {2} \nAdverb Numbers: {3}'.format(json_obj['Adjective'],json_obj['Verb'],json_obj['Noun'],json_obj['Adverb'])
#print(result_info)
wordlist = json_obj['WordList']['Adjective']
word_tmp = ''

for item in wordlist:
    word_tmp += item+'\n'

f = open('{0}_wordcloud_result.txt'.format(filename),'w+',encoding='utf-8')
f.write(word_tmp)
#print(word_tmp)
w.generate(word_tmp)

w.to_file('{0}_wordcloud_result.png'.format(filename))
