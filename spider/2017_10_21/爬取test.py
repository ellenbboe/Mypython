import re
import urllib.request

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="J_goodsList".+? <div class="page clearfix">'
    result1= re.compile(pat1).findall(html1)
    #result1= result1[0]
    pat2 ='<img width="220" height="220" class="err-product" data-img="1" src="//img(.+?\.jpg)">'
    imagelist= re.compile(pat2).findall(str(result1))
    x=1
    for imageurl in imagelist:
        imagename = "D:/j/"+str(page)+str(x)+".jpg"
        imageurl = "http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename = imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,30):
    url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page="+str(i)
    craw(url,i)
    
    
