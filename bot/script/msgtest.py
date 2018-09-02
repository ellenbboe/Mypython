# -*- coding: utf-8 -*-
import json
import random
from urllib import request
from urllib import parse

def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是超人/得意')
    elif content == '-itistimetosleep':
        bot.SendTo(contact, 'byebye/睡')
        bot.Stop()
    elif content == "名人名言":
        said = getsaids("result.json")
        bot.SendTo(contact, said)
    if '@ME' in content:
        bot.SendTo(contact, member.name+'，你好啊^-^')

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

def getweather(city):
    key = "key=823b446b4bba46299db468b9ca0f2e6a"
    city = parse.quote(city)
    location = "location="+city
    urlnow = "https://free-api.heweather.com/s6/weather/now?"+key+"&"+location
    response = request.urlopen(urlnow)
    result =response.read().decode('utf-8')
    result=json.loads(result)["HeWeather6"]
    return type(result)#字典
    # return urlnow

if __name__ == '__main__':
    print(getweather("绍兴"))