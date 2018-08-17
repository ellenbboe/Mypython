import urllib.request
url = "http://www,baidu.com"
file=urllib.request.urlopen(url)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle=open("D:/j/workplace/spiderweb/1.html","wb")
fhandle.write(data)
fhandle.close()
