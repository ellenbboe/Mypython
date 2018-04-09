# -*- coding:utf-8 -*-
# time:18-4-6
from urllib import request
class HtmlDownloader(object):
    def downloader(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode()!= 200:
            return None
        return response.read()