# Mathematical_modeling
## 美国数学建模 2020 C题

## Python 3

## 需要的环境有 numpy , Matplotlib , xlrd , pyecharts , pandas , nltk

## Linux 安装方式

> sudo pip install numpy matplotlib xlrd pyecharts pandas nltk

## Windows 安装方式 (打开 CMD 需管理员权限)

> pip install numpy matplotlib xlrd pyecharts pandas nltk

## excel.py 封装的api 示例见 sample_excel.py

## plot.py 绘图的示例

## util.py 内置两个排序函数 一个是 sort() 一个是 quickSort()

## nltk 的相关配置 [配置方法](https://blog.itjoker.cn/post/iCBxLUOlf/)

## nltk_api/Sentiment.py 为文本的情绪分析（只支持英文） 返回的是float

## nltk_api/lemmatize.py 为文本的词性分析（只支持英文） 返回的数据格式是json

## Example

```pythton

import util

data = [1,2,123,241,221,111,2,3,734534,121,222] # example data
print(util.sort(data))
print('--------')
print(util.quickSort(data))

```