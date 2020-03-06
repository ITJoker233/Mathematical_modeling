from excel import *
from pyecharts.charts import *
from pyecharts import options as opts

Title = 'xxx数据的情况'
excel = Excel('RAW_DATA/hair_dryer.xlsx')
cum = excel.readColData(8)#第9个
key = excel.keys[8]
x = []
for i in range(0,len(cum)):
    x.append(i)
print(excel.keys)
bar = ( 
    Bar()
    .add_xaxis(x)
    .add_yaxis(key,cum)
    .set_global_opts(title_opts=opts.TitleOpts(title=Title))
)
bar.render(r"result.html")