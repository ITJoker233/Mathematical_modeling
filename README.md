# Mathematical_modeling

## 美国数学建模 2020 C题

## 使用 Python 3。x 环境

## 需要的库有 numpy , Matplotlib , xlrd , pyecharts , pandas , nltk , wordcloud

## Linux 安装方式

> sudo pip install numpy matplotlib xlrd pyecharts pandas nltk wordcloud

## Windows 安装方式 (打开 CMD 需管理员权限)

> pip install numpy matplotlib xlrd pyecharts pandas nltk wordcloud

## [在线预览 pacifier_anylyz_result](https://cdn.itjoker.cn/Mathematical_modeling/pacifier_anylyz_result.html)

## [在线预览 hair_dryer_anylyz_result](https://cdn.itjoker.cn/Mathematical_modeling/hair_dryer_anylyz_result.html)

## [在线预览 microwave_anylyz_result](https://cdn.itjoker.cn/Mathematical_modeling/microwave_anylyz_result.html)

## excel.py 操作excel封装好的api 示例见 sample_excel.py

## plot.py 生成品牌情绪网页结果的程序

```python3 plot.py```

## create_wordcloud_anylyz.py 生成词云的程序，并输出到RESULT目录下

```python3 create_wordcloud_anylyz.py```

## create_sentiment_anylyz.py 分析品牌的情绪分，并输出到RESULT目录下

```python3 create_sentiment_anylyz.py```


## nltk 的相关配置 [配置方法](https://blog.itjoker.cn/post/iCBxLUOlf/)

## nltk_api/Sentiment.py 为文本的情绪分析的api（只支持英文） 返回的是dict()

## nltk_api/Lemmatize.py 为文本的词性分析的api（只支持英文） 返回的数据格式是json

## Example

```pythton

import util

data = [1,2,123,241,221,111,2,3,734534,121,222] # example data
print(util.sort(data))
print('--------')
print(util.quickSort(data))
```