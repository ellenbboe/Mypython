import urllib.request
import urllib.parse

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode( {
    "name":"ceo@iqianyue.com",
    "pass":"A123"
    } ).encode('utf-8')#将数据使用url编码处理后,使用encode()设置utf-8编码
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko')
data = urllib.request.urlopen(req).read()
fh = open("D:/j/workplace/spiderweb/posttest.html","wb")
fh.write(data)
fh.close()
