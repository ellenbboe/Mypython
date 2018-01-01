
import urllib.request
import re
def use_proxy(url):
    #仿照浏览器爬取网站(使用了代理)
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 		(KHTML, like Gecko')
	html = urllib.request.urlopen(req).read().decode('utf-8')
    #这是正则表达式
	reg = r'<a href="(.*?)" class="TypeBigPics" target="_blank"><img src=".*?" width=".*?" height=".*?" /><div class="ListTit">(.*?)</div></a>'
	pictureUrl = re.findall(reg,html)#得到的是图片的网址第一面和主题
	reg2 = r'<img alt=".*?" alt="" src="(.*?)" />'  # 得到图片的源地址 正则
	reg3 = r"<a href='(.*?)下一页</a>"  # 下一页网址 正则(error)
	reg4 = r"<a href='(.*?)'>"#re again
	mainurl = 'http://www.umei.cc'
	page = 0
	for pictureHtml in pictureUrl:#进入图片网址第一页
		print(pictureHtml[0])
		i =1
		print(i)
		html1 = urllib.request.urlopen(pictureHtml[0]).read().decode('utf-8')
		pictureurlList = re.findall(reg2, html1)#找到图片的网址 列表
		pictureName = str(pictureUrl[1][1]) + str(i) + ".jpg"
		i = i+1;
		#下载
		data = urllib.request.urlopen(pictureurlList[0]).read()
		temp_file = open(pictureName, 'wb')
		temp_file.write(data)
		temp_file.close()

		pictureNextList = re.findall(reg3, html1)#下一页网址 列表
		pictureNextList2= re.findall(reg4, pictureNextList[0])
		
		page=page+1
		while (pictureNextList2[len(pictureNextList)] !='#'):
			nexturl = mainurl + pictureNextList2[len(pictureNextList)]#构建下一页的网址
			html2 = urllib.request.urlopen(nexturl).read().decode('utf-8')
			pictureurlList1 = re.findall(reg2, html2)

			pictureName = str(pictureUrl[page][1]) + str(i) + ".jpg"
			i = i + 1;
			# 下载
			data = urllib.request.urlopen(pictureurlList1[0]).read()
			temp_file = open(pictureName, 'wb')
			temp_file.write(data)
			temp_file.close()
			pictureNextList = re.findall(reg3, html2)
			pictureNextList2= re.findall(reg4, pictureNextList[0])






        # print(pictureHtml[0])
    # return urlList

url = "http://www.umei.cc/meinvtupian/"
#def getpictureUrl():

use_proxy(url)
#print(data)
# fh = open('D:/123.html','wb')
# fh.write(data)
# fh.close()
#getpictureUrl()
