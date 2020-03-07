from requests import get
from requests import post
import json 

def emotion_anylyz(msg):
    postData = {'data': msg}
    response = post('https://bosonnlp.com/analysis/sentiment?analysisType=', data=postData)
    data = response.text
    now_mod_rank = int(float(data.replace("[","").replace("]","").split(',')[0])*100)
    str_now_mod_rank = str(now_mod_rank) + "%" # 情感评分指数(越接近1表示心情越好，越接近0表示心情越差)
    mood_message = u"message:\n{0}\nemotion_rank:{1}\n".format(msg ,str_now_mod_rank)
    return mood_message