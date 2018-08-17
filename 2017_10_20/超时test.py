import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://www.baidu.com",timeout = 1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("异常为->"+e)
