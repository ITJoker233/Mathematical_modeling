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

sentence = "This dries my hair faster that bigger, more powerful models. I love travel blow dryers because they are easy to lift and they usually come in 1600 w or less. Bigger dryers are heavy and blow my hair everywhere. This has a surprising amount of power and is very compact. I would give it a five except that the switch is not easy to turn on and off with one hand and it's noisier than I anticipated."

print(emotion_anylyz(sentence))
