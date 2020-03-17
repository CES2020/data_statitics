#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: coord_format_convert.py 
@time: 2020/03/16
将 Excel 表里的坐标数据转换格式
"""

import pandas as pd
import numpy as np


df = pd.read_excel('place_location2.xlsx')
for i in range(0, len(df)):
    print('\'', df.loc[i][0],'\'', ':[', df.loc[i][1], ',', df.loc[i][2], ']' ,',', sep='')


# fo = open('name_value.json', 'r+')
# fo.write(result_json)