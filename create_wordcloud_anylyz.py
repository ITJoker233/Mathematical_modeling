from excel import *
import wordcloud,json , os, os.path,time
import  nltk_api.Lemmatize as Lemmatize

w = wordcloud.WordCloud(max_words=200,width=800,height=400,margin=5,background_color='white')

def IsSubString(SubStrList,Str):
    flag=True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False

    return flag

def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (len(FlagStr)>0):
               #返回指定类型的文件名
               if (IsSubString(FlagStr,fn)):
                   fullfilename=os.path.join(FindPath,fn)
                   FileList.append(fullfilename)
           else:
               #默认直接返回所有文件名
               fullfilename=os.path.join(FindPath,fn)
               FileList.append(fullfilename)
    #对文件名排序
    if (len(FileList)>0):
        FileList.sort()

    return FileList

def create(filename):
    excel = Excel('{0}'.format(filename))
    reviews = excel.readColData(13) #列数 从0开始
    sentence_list = ''
    for item in reviews:
        sentence_list += item + '\n'
    json_obj = json.loads(Lemmatize.anylyz(sentence_list))

    result_info = 'Adjective Numbers: {0} \nVerb Numbers: {1} \nNoun Numbers: {2} \nAdverb Numbers: {3}'.format(json_obj['Adjective'],json_obj['Verb'],json_obj['Noun'],json_obj['Adverb'])
    #print(result_info)
    filename = filename.split('\\')[1]
    filename = filename.replace('SORT_DATA\\\\','')
    f = open('RESULT\\{0}_wordcloud_result.txt'.format(filename),'w+',encoding='utf-8')
    f.write(result_info)

    wordlist = json_obj['WordList']['Adjective']
    word_tmp = ''
    for item in wordlist:
        word_tmp += item+'\n'
    #print(word_tmp)
    w.generate(word_tmp)
    w.to_file('RESULT\\{0}_wordcloud_result.png'.format(filename))
print('Starting....')
paths = (GetFileList('SORT_DATA'))
print('Get File List Success!')
for path in paths:
    old_time = time.time()
    path = path.replace('\\','\\')
    create(path)
    print('>>> [ {0} ] Create_WordCloud used_time: {1} ms'.format(path,float((time.time()-old_time)*1000)))