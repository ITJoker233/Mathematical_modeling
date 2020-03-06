from excel import *

if __name__ == '__main__':
    filePath = r'RAW_DATA/吹风机.xlsx'
    data = Excel(filePath)
    # 打印最后信息
    print(data.dict_data())