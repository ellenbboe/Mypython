# -*- coding:utf-8 -*-
# time:18-4-6
from ho import html_downloader,url_manage,html_output,html_parser
class spidermain():
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d:%s\n"%(count,new_url))
                count+=1
                html_cont = self.downloader.downloader(new_url)
                new_urls,new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 3:
                    break
            except:
                print("craw failed")

        self.output.output_html()



if __name__ =="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313.html"
    obj_spider = spidermain()
    obj_spider.craw(root_url)
