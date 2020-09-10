from excel import *
from utils import *
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

'''建立对应的每个宿舍的用水量字典文件'''
def createDict(read_file_path,save_file_path):
    excel = Excel(read_file_path)
    excel_dicts = excel.dict_data()
    water_meter_name = excel_dicts[0]['水表名'] # 默认设置为第一行的第一个水表名
    object_dict = {
        'name':'',
        'date':[],
        'usageAmount':[],
        'sum':0
    }
    for dict_ in excel_dicts:
        if dict_['水表名'] == water_meter_name:
            object_dict['name'] = water_meter_name
            object_dict['usageAmount'].append(dict_['用量'])
            object_dict['date'].append(dict_['采集时间'])
            object_dict['sum'] += dict_['用量']
        else:
            writeFile(save_file_path+water_meter_name+'.json',json.dumps(object_dict))
            print(f'create {water_meter_name} Dict success!')
            water_meter_name = dict_['水表名']
            object_dict['name'] = water_meter_name
            object_dict['usageAmount'] = []
            object_dict['date'] = []
            object_dict['sum'] = 0
            object_dict['usageAmount'].append(dict_['用量'])
            object_dict['date'].append(dict_['采集时间'])
            object_dict['sum'] += dict_['用量']
    writeFile(save_file_path+water_meter_name+'.json',json.dumps(object_dict))
    print('Create Dict Success!')

def getDirFilePathList(dirname):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)
    return result

'''
以分析第一季度的宿舍用水量为例
当前先获取到所有宿舍的用水情况,取第一季数据为例
'''
if __name__ == "__main__":
    read_base_path='RAW_DATA/'
    save_base_path='RESULT/' 
    file_name = '第一季度_宿舍.xlsx'
    read_file_path = f'{read_base_path}{file_name}'
    save_file_path = f'{save_base_path}the_first_quarter/'# 存储到第一季度目录下
    createDict(read_file_path,save_file_path)
    filePaths = getDirFilePathList(save_file_path)
    for filePath in filePaths:
        if filePath != '' and filePath.endswith('json'):
            json_obj = json.loads(readFile(filePath))
            data = json_obj['usageAmount']
            dates = json_obj['date']
            print(f'Starting {filePath}')
            createChart(data,dates,f'{json_obj["name"]}_用水情况',save_file_path)