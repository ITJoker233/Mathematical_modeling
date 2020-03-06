# Mathematical_modeling
## 美国数学建模 2020 C题

## Python 3

## 需要的环境有 numpy , Matplotlib , xlrd , pyecharts , pandas

## Linux 安装方式

>  sudo pip install numpy matplotlib xlrd pyecharts pandas

## Windows 安装方式 (打开 CMD 需管理员权限)

> pip install numpy matplotlib xlrd pyecharts pandas

## excel.py 封装的api 示例见 sample_excel.py

## plot.py 绘图的示例

## util.py 内置两个排序函数 一个是 sort() 一个是 quickSort()

## Example:
```pythton
import util

data = [1,2,123,241,221,111,2,3,734534,121,222] # example data
print(util.sort(data))
print('--------')
print(util.quickSort(data))
```