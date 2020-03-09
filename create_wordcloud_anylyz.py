from excel import *
import wordcloud,json , os, os.path,time
import  nltk_api.Lemmatize as Lemmatize

w = wordcloud.WordCloud(max_words=200,width=800,height=400,margin=5,background_color='white')

def getAllPath(dirname):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)
    return result

def create(filepath):
    excel = Excel('{0}'.format(filepath))
    reviews = excel.readColData(13) #列数 从0开始
    sentence_list = ''
    for item in reviews:
        sentence_list += str(item) + '\n'
    json_obj = json.loads(Lemmatize.anylyz(sentence_list))

    result_info = 'Adjective Numbers: {0} \nVerb Numbers: {1} \nNoun Numbers: {2} \nAdverb Numbers: {3}'.format(json_obj['Adjective'],json_obj['Verb'],json_obj['Noun'],json_obj['Adverb'])
    #print(result_info)
    filename = filepath.split('\\')[2]
    save_dirpath = filepath.split('\\')[1]
    f = open(r'RESULT\{0}\wordcloud_{1}_result.txt'.format(save_dirpath,filename),'w+',encoding='utf-8')
    f.write(result_info)
    f.close()
    wordlist = json_obj['WordList']['Adjective']
    word_tmp = ''
    for item in wordlist:
        word_tmp += item+'\n'
    #print(word_tmp)
    w.generate(word_tmp)
    w.to_file(r'RESULT\{0}\wordcloud_{1}_result.png'.format(save_dirpath,filename))
print('Starting....')
paths = getAllPath('SORT_DATA')#(GetFileList('SORT_DATA\\'))
print('Get File List Success!')
for path in paths:
    old_time = time.time()
    path = path.replace('\\','\\')
    create(path)
    print('>>> [ {0} ] Create_WordCloud used_time: {1} ms'.format(path,float((time.time()-old_time)*1000)))