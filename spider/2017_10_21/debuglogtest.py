import urllib.request

httphd = urllib.request.HTTPHandler(debuglevel = 1)
httpshd = urllib.request.HTTPSHandler(debuglevel = 1)

opener  = urllib.request.build_opener(httphd,httpshd)
#创建opener对象设置参数
urllib.request.install_opener(opener)
#安装opener,当使用urlopen时会使用安装的opener
data = urllib.request.urlopen("http://www.baidu.com")
