from excel import *
from utils import *
import json,time

magage_keywords = '宿舍'
chinese_nums = ['一','二','三','四']
raw_data_path = 'RAW_DATA/附件_{0}季度.xlsx'
save_file_path = f'RAW_DATA/预处理_{magage_keywords}.json'

all_data = {
    '第一季度':[],
    '第二季度':[],
    '第三季度':[],
    '第四季度':[],
}
for chinese_num in chinese_nums:
    excel = Excel('RAW_DATA/第一季度_宿舍.xlsx',read_only=True)#Excel(raw_data_path.format(chinese_num),read_only=True)
    oldTime = time.time()
    excel_dicts = excel.dict_data()
    print(excel_dicts)
    exit(0)
    print(f'第{chinese_num}季度 数据读取完成')
    for excel_dict in excel_dicts:
        if magage_keywords in excel_dict['水表名']:
            print(f'{excel_dict["水表名"]}')
            all_data[f'第{chinese_num}季度'].append(excel_dict)
writeFile(save_file_path.format(magage_keywords),json.dumps(all_data))