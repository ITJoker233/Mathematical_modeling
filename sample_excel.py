import excel

if __name__ == '__main__':
    filename = r'RAW_DATA/吹风机.xlsx'
    host_sheet, rows = excel.open(filename)
    host_datas = excel.read(host_sheet, rows)
    print(host_datas)
