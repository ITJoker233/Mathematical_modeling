#!/usr/bin/env python
# coding=utf-8
# 封装实现读取表格数据
# 优化了xlrd中单元格的数据类型：
'''
    数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
    成我们想要的数据类型
    0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''
 
import xlrd
from xlrd import xldate_as_tuple
import datetime
 
class Excel:
    # def __init__(self, excel_path, sheet_name):
    def __init__(self, excel_path):
        self.data = xlrd.open_workbook(excel_path)
        #self.table = self.data.sheet_by_name(sheet_name) # 这个可以根据传入进来的sheet表名字来获取
        self.table = self.data.sheets()[0] # 直接获取第一个sheet表
        self.keys = self.table.row_values(0) # 获取第一行作为key值
        self.rowNum = self.table.nrows # 获取总行数
        self.colNum = self.table.ncols # 获取总列数
 
    def dict_data(self):
        if self.rowNum <= 1:
            print("Total less than 1")
        else:
            print('keys: {0} \n\n > rowNum: {1} colNum: {2} \n\n'.format(self.keys,self.rowNum,self.colNum))
            r = []
            j = 1 # 第一行
            for i in range(self.rowNum - 1): # 减1防止越界，从第一行开始的，不是从0行开始，所以总数减1
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum): # x列
                    c_type = self.table.cell(j, x).ctype # 获取单元格数据类型
                    c_cell = self.table.cell_value(j,x) # 获取单元格数据
                    if c_type == 2 and c_cell % 1 == 0: # 如果是整形
                        values[x] = int(values[x])
                    elif c_type == 3: # 日期
                        date = datetime.datetime(*xldate_as_tuple(c_cell, 0)) # 转成datetime对象
                        values[x] = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif c_type == 4: # 布尔类型
                        values[x] = True if c_cell == 1 else False
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r