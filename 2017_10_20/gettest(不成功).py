import urllib.request

url1 = "https://www.baidu.com?&wd="
key1 = "lol"
url_one = url1 + key1
req1 = urllib.request.Request(url_one)
data1= urllib.request.urlopen(req1).read()
fh1 = open("D:/j/workplace/spiderweb/gettest1.html","wb")
fh1.write(data1)
fh1.close()


url2 = "https://www.baidu.com?&wd="
key2 = "英雄联盟"
key2_code = urllib.request.quote(key2)#进行编码
url_two = url2 + key2_code
req2 = urllib.request.Request(url_two)
data2 = urllib.request.urlopen(req2).read()
fh1 = open("D:/j/workplace/spiderweb/gettest2.html","wb")
fh1.write(data2)
fh1.close()


