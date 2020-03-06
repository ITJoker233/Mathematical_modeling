import xlrd 

def open(filename):
    workbook = xlrd.open_workbook(filename)
    # 获取全部工作表（sheet）以及选取对应的工作表
    sheet_name = workbook.sheet_names()[0]
    host_sheet = workbook.sheet_by_name(sheet_name)
    rows = host_sheet.nrows
    return host_sheet, rows

def read(host_sheet, rows):
    host_data = []
    for row in range(rows):
        host_data += [host_sheet.row_values(row)]
    return host_data[1:]

