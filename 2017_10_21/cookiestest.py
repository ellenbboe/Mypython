import urllib.request
import urllib.parse
import http.cookiejar
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LImMb"

postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
    }).encode('utf-8')
req = urllib.request.Request(url,postdata)

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()

fh = open("D://j/workplace/spiderweb/1.html","wb")
fh.write(data)
fh.close()

url2 = "http://bbs.chinaunix.net/"

data2 = urllib.request.urlopen(url2).read()
fh2 = open("D://j/workplace/spiderweb/2.html","wb")
fh2.write(data2)
fh2.close()
