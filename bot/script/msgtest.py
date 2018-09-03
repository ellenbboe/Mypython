# -*- coding: utf-8 -*-

'''
功能简介:
发送 天气-城市 得到天气预报
发送 名人名言 得到json中随机数据
发送 脑筋急转弯 得到json中随机数据
发送 答案-数字 得到脑筋急转弯的答案
发送 随机一文 得到文章一篇
'''


import json
import re
import random
from urllib import request
from urllib import parse
from urllib.request import FancyURLopener
def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是天晴/得意')
    elif content == '-itistimetosleep':
        bot.SendTo(contact, 'byebye/睡')
        bot.Stop()
    elif content == '脑筋急转弯':
        question = havearest_question("zhiliti.json")
        bot.SendTo(contact, question)
    elif content == '随机一文':
        article = randomarticle()
        bot.SendTo(contact, article)
    elif re.match("答案-([0-9]+)?",content):
        num = re.match("答案-([0-9]+)?",content).group(1)
        answer = havearest_answer(num)
        bot.SendTo(contact, answer)
    elif content == "名人名言":
        result = getsaids("juzimi.json")
        bot.SendTo(contact, result)
    elif re.match("天气-([\u4E00-\u9FA5]+)?",content):
        reobject = re.match("天气-([\u4E00-\u9FA5]+)?",content)
        result = getweather(reobject.group(1))
        bot.SendTo(contact, result)
    if '@ME' in content:
        content = content.replace("@天晴","")
        answer = tulingrobot(content)
        bot.SendTo(contact, member.name+','+answer)

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
#---------------------------------------------------------
#--------------------------------------------------------
# 脑筋急转弯
def havearest_question(filename):
    with open(filename,'r') as f:
        file = json.loads(f.read())
    lucknum = random.randint(0, len(file))
    description = file[lucknum]['description'][0]
    return description+"   --------想要答案的话和我说:答案-"+str(lucknum)

def havearest_answer(lucknum):
    with open("zhiliti.json",'r') as f:
        file = json.loads(f.read())

    if(int(lucknum) > len(file)):
        return "没有这一题的答案哦"
    answer = file[int(lucknum)]['answer']
    return answer
#---------------------------------------------------------
#--------------------------------------------------------
#随机文章
def randomarticle():
    # url="https://interface.meiriyiwen.com/article/random?dev=1"
    # print(url)
    class MyOpener(FancyURLopener):
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'  # Set this to a string you want for your user agent

    myopener = MyOpener()
    response = myopener.open('https://interface.meiriyiwen.com/article/random?dev=1')
    # response = request.urlopen(url)
    result = json.loads(response.read().decode('unicode_escape'))
    author = "作者: "+result["data"]["author"]
    title =" 标题: " +result["data"]["title"]
    wc = " 全文字数: "+str(result["data"]["wc"])
    digest =" 简要内容如下: "+result["data"]["digest"]
    return author+title+wc+digest
#---------------------------------------------------------
#--------------------------------------------------------
#图灵机器人
def tulingrobot(somthing):
    somthing = parse.quote(somthing)
    url="http://www.tuling123.com/openapi/api?key=90c391a54e4741759d1abd84a0f45f7a&info="
    url=url+somthing
    response = request.urlopen(url)
    result = json.loads(response.read())
    if(result['code']!=100000):
        return "恩..你可能需要百度一下"
    return result['text']

# if __name__ == '__main__':
#     print(tulingrobot("我爱你"))