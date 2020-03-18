#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: crawler_demo.py 
@time: 2020/03/18 
"""

import requests
import json

def parse_url(data={}):
    """
    拼接url地址，森林防火项目时写的函数
    """
    item = data.items()
    urls= '?'
    for i in item:
        (key, value) = i
        temp_str = key + "=" + "%s" % value
        urls = urls + temp_str + "&"
    urls = urls[:len(urls) - 1]
    return urls

if __name__ == "__main__":
    baseurl = 'http://api.map.baidu.com/geocoding/v3/'
    address = '湖南大学'
    params = {
        'address': '湖南省长沙市' + address,  # 地址
        'output': 'json',
        'ak': 'exA7IllQD32dPVgPlMx5kP34j4dAvokQ'}  # 百度密钥 峰值接受每秒200次请求。
    url = baseurl + parse_url(params)

    res = requests.get(url)
    # print(res.text)
    jd = json.loads(res.text)
    coords = jd['result']['location']
    print(coords)