#!/usr/bin/env python3

import sys
import os
import json
import re
from urllib import request

#---------------------------
# 读出文件 cat
#---------------------------
def readfile():
    filename=input("输入文件名称:")
    print("-----文件名: "+filename+"-------")
    with open(filename, 'r') as f:
        file = f.read()
    print(file)
    print("--------文档结束-------")
#---------------------------
# 删除文件 rm
#---------------------------

def delectfile():
    filename = input("输入文件名称:")
    print("----删除文件-----")
    os.remove(filename)
    print("-----已删除------")
#---------------------------
#  重命名文件 mv
#---------------------------
def renamefile():
    srcname = input("输入原文件名称:")
    dicname = input("输入更改名称:")
    print("-----重命名-------")
    os.renames(srcname,dicname)
    print("原来名称: "+srcname)
    print("目前名称: "+dicname)
    print("-----已完成-------")
#---------------------------
# 列出文件 ls
#---------------------------
def listfiles():
    nowdir = input("输入目录:")
    d=os.listdir(nowdir)
    for part in d:
        print(part)
    print("-----done-----")
#---------------------------
# mkdir
#---------------------------
def makedir():
    checkdir= input("输入要创建的文件夹的名称:")
    if( os.path.exists(checkdir)):
        print("----文件夹已存在----")
    else:
        os.mkdir(checkdir)
        print("----文件夹已创建----")


