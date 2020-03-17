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
    """
    item = data.items()
    urls= '?'
    for i in item:
        (key, value) = i
        temp_str = key + "=" + "%s" % value
        urls = urls + temp_str + "&"
    urls = urls[:len(urls) - 1]
    return urls


def get_locate(data_in, file_out):
    """
    爬虫函数
    data_in 为列表
    file_out 为文件对象
    """
    for index in range(len(data_in)):
        line = data_in[index]
        address = line

        baseurl = 'http://api.map.baidu.com/geocoding/v3/'
        params = {
            'address': '湖南省长沙市' + address,  # 地址
            'output': 'json',
            'ak': 'exA7IllQD32dPVgPlMx5kP34j4dAvokQ'}  # 百度密钥 峰值接受每秒200次请求。
        url = baseurl + parse_url(params)

        res = requests.get(url)
        jd = json.loads(res.text)
        coords = jd['result']['location']
        if address == '科大一号院':
            coords['lng'] = 113.00650
            coords['lat'] = 28.23198

        out_loc = '\'' + address + '\'' + ':[' + str(round(coords['lng'], 5)) + ',' + str(
            round(coords['lat'], 5)) + '], \n'
        file_out.write(out_loc)

if __name__ == "__main__":
    # 地址输入，一行一个地址
    f = io.open('place_dup.csv', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    # 输出文档
    f_out = open('loc.txt', 'r+')
    f_out.truncate(0)

    urlList = []
    if (data.find('"') != -1):
        data = data.replace('"', '')
    datas = data.split('\n')

    # print(datas)
    get_locate(datas, f_out)


