import urllib.request
import re
def use_proxy(url):
    #仿照浏览器爬取网站(使用了代理)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko')
    html = urllib.request.urlopen(req).read().decode('utf-8')
    #这是正则表达式
    reg = r'<span class=".*?"><a href="http://www.hunter-its.com/pic/(.*?)/1.html" target="_blank">(.*?)</a></span>'
    urlList = re.findall(reg,html)
    reg2 = r'<a><img src="(.*?)" width=".*?"></a>'
    mainurl = 'http://www.hunter-its.com/pic/'
    for pictureHtml in urlList:
        for i in range(1,9):
            pictureHtml1 = mainurl + str(pictureHtml[0]) + '/' + str(i) + ".html"#遍历页面
            html1 = urllib.request.urlopen(pictureHtml1).read().decode('utf-8')
            pictureurl = re.findall(reg2, html1)

            # break;
            pictureName =  str(pictureHtml[1]) + str(i) + ".jpg"
            data = urllib.request.urlopen(pictureurl[0]).read()
            temp_file = open(pictureName, 'wb')
            temp_file.write(data)
            temp_file.close()


        # print(pictureHtml[0])
    # return urlList


url = "http://www.hunter-its.com"
#def getpictureUrl():
#proxy_addr = "115.210.75.149:34485"
use_proxy(url)
#print(data)
# fh = open('D:/123.html','wb')
# fh.write(data)
# fh.close()
#getpictureUrl()
