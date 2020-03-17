#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: get_baidu_coord.py 
@time: 2020/03/17
采用百度地图API进行地理编码
"""

import io
import requests
import json

def parse_url(data={}):
    """
    拼接url地址，森林防火项目时写的函数
    """"
    item = data.items()
    urls= '?'
    for i in item:
        (key, value) = i
        temp_str = key + "=" + "%s" % value
        urls = urls + temp_str + "&"
    urls = urls[:len(urls) - 1]
    return urls

# 地址输入，一行一个地址
f = io.open('place_dup.csv', 'r', encoding='utf-8')
data = f.read()
f.close()

# 输出文档
f_out = open('loc.txt', 'r+')
f_out.truncate(0)


urlList = []
if(data.find('"') != -1):
    data = data.replace('"','')
datas=data.split('\n')

# print(datas)

for index in range(len(datas)):
    line = datas[index]
    address = line

    baseurl = 'http://api.map.baidu.com/geocoding/v3/'
    params = {
        'address' : '湖南省长沙市' + address,   # 地址
        'output': 'json' ,
        'ak' : 'exA7IllQD32dPVgPlMx5kP34j4dAvokQ'}   # 百度密钥
    url= baseurl+ parse_url(params)

    res = requests.get(url)
    jd = json.loads(res.text)
    coords = jd['result']['location']
    out_loc = address +
    print(coords)


# url = 'http://api.map.baidu.com/geocoder/v3/'
# params = { 'address' : '启东市',           # 以江苏省启东市为例
#            'ak' : 'exA7IllQD32dPVgPlMx5kP34j4dAvokQ',          # 百度密钥
#            'output': 'json'     }          # 输出结果设置为json格式
# res = requests.get('http://api.map.baidu.com/geocoding/v3/?address=北京市海淀区上地十街10号&output=json&ak=exA7IllQD32dPVgPlMx5kP34j4dAvokQ&callback=showLocation //GET请求')
# print(res.text)