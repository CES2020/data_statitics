#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: get_baidu_coord.py 
@time: 2020/03/17 
"""

import io

f = io.open('place_dup.csv', 'r', encoding='utf-8')
data = f.read()

urlList = []


if(data.find('"') != -1):
    data = data.replace('"','')
datas=data.split('\n')

f.close()

print(datas)