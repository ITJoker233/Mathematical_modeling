from excel import *

if __name__ == '__main__':
    filePath = r'RAW_DATA/hair_dryer.xlsx' #吹风机
    data = Excel(filePath)
    # 打印最后信息
    print(data.dict_data())