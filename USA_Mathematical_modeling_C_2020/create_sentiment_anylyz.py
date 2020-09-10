from excel import *
import json , os, os.path,time
import  nltk_api.Sentiment as Sentiment

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
    kvp = Sentiment.anylyz(reviews)
    filename = filepath.split('\\')[2]
    save_dirpath = filepath.split('\\')[1]
    with open(r'RESULT\{0}\sentiment_{1}_result.json'.format(save_dirpath,filename),"w") as f:
        json.dump(kvp,f)
    f.close()
    print('Sentiment Rank: {0}'.format(kvp['sum']))
print('Starting....')
paths = getAllPath('SORT_DATA')#(GetFileList('SORT_DATA\\'))
print('Get File List Success!')
for path in paths:
    old_time = time.time()
    path = path.replace('\\','\\')
    create(path)
    print('>>> [ {0} ] Create_Sentiment used_time: {1} ms'.format(path,float((time.time()-old_time)*1000)))