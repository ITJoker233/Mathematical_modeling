import json , os, os.path,time,re
from pyecharts.charts import *
from pyecharts import options as opts

def getAllPath(dirname):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)
    return result

def readfile(filepath):
    f = open(filepath,'r+')
    result = f.read()
    f.close()
    return result

def create(anylyz_list,anylyz_name,anylyz_type):
    Title = '{0}_Emotional_Scores'.format(anylyz_type)
    x = [] 
    data = []
    for i in range(0,len(anylyz_name)):
        x.append(anylyz_name)
        json_data = readfile(anylyz_list[i])
        json_obj = json.loads(json_data)
        data.append(round(json_obj['sum'],2))
    bar = ( 
        Bar()
        .add_xaxis(x)
        .add_yaxis(anylyz_type,data)
        .set_global_opts(title_opts=opts.TitleOpts(title=Title))
    )
    bar.render('{0}_anylyz_result.html'.format(anylyz_type))

filepaths = getAllPath('RESULT')
pattern = '.*?json'
pattern_1 = 'sentiment_hair_dryer_(.*?).xlsx_result.json'
pattern_2 = 'sentiment_microwave_(.*?).xlsx_result.json'
pattern_3 = 'sentiment_pacifier_(.*?).xlsx_result.json'
anylyz_list = {'hair_dryer':[],'pacifier':[],'microwave':[]}
anylyz_name_list = {'hair_dryer':[],'pacifier':[],'microwave':[]}
for filepath in filepaths:
    filename = filepath.split('\\')[2]
    anylyz_type = filepath.split('\\')[1]
    if(re.match(pattern,filename)):
        if(anylyz_type == 'hair_dryer'):
            anylyz_name_list['hair_dryer'].append(re.findall(pattern_1,filename)[0])
            anylyz_list['hair_dryer'].append(filepath)
        elif(anylyz_type == 'microwave'):
            anylyz_name_list['microwave'].append(re.findall(pattern_2,filename)[0])
            anylyz_list['microwave'].append(filepath)
        elif(anylyz_type == 'pacifier'):
            anylyz_name_list['pacifier'].append(re.findall(pattern_3,filename)[0])
            anylyz_list['pacifier'].append(filepath)
print('Creating hair_dryer Result...')
create(anylyz_list['hair_dryer'],anylyz_name_list['hair_dryer'],'hair_dryer')
print('Creating pacifier Result...')
create(anylyz_list['pacifier'],anylyz_name_list['pacifier'],'pacifier')
print('Creating microwave Result...')
create(anylyz_list['microwave'],anylyz_name_list['microwave'],'microwave')