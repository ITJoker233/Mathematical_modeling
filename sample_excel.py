from excel import *

if __name__ == '__main__':
    filePath = r'RAW_DATA/hair_dryer.xlsx' #吹风机的数据存在的目录
    data = Excel(filePath) # 建立一个Excel的操作实例
    data_ = data.readColData(1) #获取第一列的数据
    print(data_) #输出第一列的数据
    data_ = data.readRowData(1) #获取第一行的数据
    print(data_) #输出第一行的数据
    ## 使用属性的方法获取
    print(data.rowNum) #输出总行数
    print(data.colNum) #输出总列数
    print(data.keys)  #输出所有键值
    ## 使用方法获取
    print(data.getRowNum) #输出总行数
    print(data.colNum) #输出总列数
    print(data.keys) #输出所有键值