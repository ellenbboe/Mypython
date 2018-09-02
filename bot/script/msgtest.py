# -*- coding: utf-8 -*-
import json
import re
import random
from urllib import request
from urllib import parse

def onQQMessage(bot, contact, member, content):
    if content == '-hello' or content == 'hello' or contact=="你好":
        bot.SendTo(contact, '你好，我是天晴/得意')
    elif content == '-itistimetosleep':
        bot.SendTo(contact, 'byebye/睡')
        bot.Stop()
    elif content == "名人名言":
        result = getsaids("result.json")
        bot.SendTo(contact, result)
    elif re.match("天气-([\u4E00-\u9FA5]+)?",content):
        reobject = re.match("天气-([\u4E00-\u9FA5]+)?",content)
        result = getweather(reobject.group(1))
        bot.SendTo(contact, result)
    if '@ME' in content:
        bot.SendTo(contact, member.name+'，你好啊^-^')

#---------------------------------------------------------
#--------------------------------------------------------
# 获取名人名言
def getsaids(filename):
    with open(filename,'r') as f:
        file = json.loads(f.read())
    lucknum = random.randint(0, len(file))
    description = file[lucknum]['description']
    tempstr=""
    for i in range(len(description)):
        tempstr = tempstr+description[i]

    description = tempstr.replace("\r"," ")
    author = file[lucknum]['author']
    if(author == None):
        author = "佚名"
    return description+"----"+author
#---------------------------------------------------------
#--------------------------------------------------------
    # 获取当天天气
def getweather(city):
    key = "key=823b446b4bba46299db468b9ca0f2e6a"
    city = parse.quote(city)#城市名称
    location = "location="+city
    urlnow = "https://free-api.heweather.com/s6/weather/now?"+key+"&"+location
    urlliftstyle = "https://free-api.heweather.com/s6/weather/lifestyle?"+key+"&"+location
    #获取实时天气数据
    response = request.urlopen(urlnow)
    result =response.read().decode('utf-8')
    result=json.loads(result)["HeWeather6"][0]
    status = result['status']#ok
    if(status != "ok"):
        return "这个城市似乎被毁灭了0.0"
    now = result['now']
    cond_txt = "天气状况:"+now['cond_txt']
    fl = " 体感温度:"+now['fl']#体感温度
    tmp = " 环境温度:"+now['tmp']#温度
    nowweather=cond_txt+fl+tmp
    #---------------------------------------------------------
    #--------------------------------------------------------
        # 获取当天天气建议
    response = request.urlopen(urlliftstyle)
    result = response.read().decode('utf-8')
    result = json.loads(result)["HeWeather6"][0]['lifestyle']#得到当天的所有建议
    advice = ''
    for i in range(len(result)):
        advice=advice+result[i]['txt']+" "

    return nowweather+"  ---我的建议是: "+advice

def havearest():
    pass
# if __name__ == '__main__':
#     print(getweather("天气-北京?"))