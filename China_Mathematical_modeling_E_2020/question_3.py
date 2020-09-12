from excel import *
from utils import *
import csv
import json,os,os.path,time,re
from pyecharts.charts import *
from pyecharts import options as opts


'''
建立折线图表
'''
def createChart(analyse_data,x_coordinate_names,y_coordinate_name,save_file_path):
    Title = f'{y_coordinate_name}_analyse'
    x = [] 
    y = []
    i = 0
    for data in analyse_data:
        x.append(x_coordinate_names[i])
        y.append(round(int(data),2))
        i += 1
    bar = ( 
        Bar()
        .add_xaxis(x)
        .add_yaxis(y_coordinate_name,y)
        .set_global_opts(title_opts=opts.TitleOpts(title=Title))
    )
    bar.render(f'{save_file_path}{y_coordinate_name}_result.html')
    print(f'Create {y_coordinate_name}_result.html Chart Success!')


def getDirFilePathList(dirname):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)
    return result

'''建立对应的每个宿舍的用水量字典文件'''
def createDict(read_file_path,save_file_path,save_file_name):
    print(f'Opening Excel {read_file_path}')
    excel = Excel(read_file_path)
    print('Starting Create Dict')
    excel_dicts = excel.dict_data()
    water_meter_name = excel_dicts[0]['水表名'].replace('\t','').replace('+','') # 默认设置为第一行的第一个水表名
    cmp_date = time.strftime('%Y-%m-%d', time.strptime(excel_dicts[0]['采集时间'], '%Y/%m/%d %H:%M:%S'))
    object_dict = {
        'date':{},
        'total':0,
        'average':0.0
    }
    for dict_ in excel_dicts:
        object_dict['total'] += dict_['用量']
        if cmp_date == time.strftime('%Y-%m-%d', time.strptime(dict_['采集时间'], '%Y/%m/%d %H:%M:%S')):
            if cmp_date in object_dict['date']:
                object_dict['date'][cmp_date] += dict_['用量']
            else:
                object_dict['date'][cmp_date] = dict_['用量']
        else:
            cmp_date = time.strftime('%Y-%m-%d', time.strptime(dict_['采集时间'], '%Y/%m/%d %H:%M:%S'))
            if cmp_date in object_dict['date']:
                object_dict['date'][cmp_date] += dict_['用量']
            else:
                object_dict['date'][cmp_date] = dict_['用量']
    object_dict['average'] = float(object_dict['total'] / len(object_dict['date']))
    writeFile(save_file_path+save_file_name+water_meter_name+'.json',json.dumps(object_dict))
    print('Create Dict Success!')

if __name__ == '__main__':
    old_time = time.time()
    read_base_path='RAW_DATA/question_3/'
    save_file_path = 'RESULT/question_3/'
    files= getDirFilePathList(read_base_path)
    for file in files:
        if file.endswith('xlsx'):
            file_name = re.findall(r'3/(.*?)\.',file)[0]
            createDict(file,save_file_path,file_name)
    files= getDirFilePathList(save_file_path)
    for file in files:
        if file.endswith('json'):
            save_name = re.findall(r'3/(.*?)\.',file)[0]+'(天)用水量'
            json_obj = json.loads(readFile(file))
            with open(f'{save_file_path}{save_name}.csv','w') as csvfile: 
                writer = csv.writer(csvfile)
                writer.writerow(['日期','（天）用水量','总量','平均'])
                flag = True
                for date in json_obj['date']:
                    if flag:
                        flag = False
                        writer.writerow([date,json_obj['date'][date],json_obj['total'],json_obj['average']])
                    writer.writerow([date,json_obj['date'][date]])
    print(f'用时:{str(int(time.time()-old_time))}s')
    '''
    for file in files:
        y_data = []
        x_name = []
        y_name = re.findall(r'3/(.*?)\.',file)[0]+'(天)用水量'
        json_obj = json.loads(readFile(file))
        for date in json_obj['date']:
            y_data.append(json_obj['date'][date])
            x_name.append(date)
        y_data.append(json_obj['average'])
        x_name.append('average')
        y_data.append(json_obj['total'])
        x_name.append('total')
        createChart(y_data,x_name,y_name,save_file_path)
    '''
