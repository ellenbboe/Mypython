import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen("https://sspai123.com/").read()
    fh = open("D://j/workplace/spiderweb/13.html","wb")
    fh.write(data)
    fh.close()
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)
#如果子类处理不了就交给父类处理
#第二种方式
#except urllib.error.URLError as e:
 #   if hasattr(e,"code"):
  #      print(e.code)
 #   if hasattr(e,"reason"):
  #      print(e.reason)
