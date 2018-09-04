def writefiles(src,Suffix):
    # Suffix = input("后缀名称:")
    # src = input("json文件路径:")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    with open(src,'r') as f:
        file = json.loads(f.read())
    for i in range(2):#max = len(file)
        name = re.sub("[A-Za-z0-9\!\%\(\)\/\[\]\,\，\。\©\s]", "", file[i]['description'])+ Suffix
        print(file[i]['src'])
        req = request.Request(url=file[i]['src'], headers=headers)
        data =request.urlopen(req).read()

        with open(name,'wb') as a:
            a.write(data)

if __name__ == '__main__':
    writefiles("result.json",".jpg")
