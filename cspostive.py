#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: cspostive.py 
@time: 2020/03/17
处理有新冠换着的小区 位置信息
"""

import pandas as pd
import numpy as np

df = pd.read_csv('CS_postive_name.txt', header= None)
df.columns=['name']
df['value'] = 1

fo = open('CSpos_name_value.txt', 'r+')
fo.truncate(0)

for i in range(len(df)):
    fo.write('{name: \'')
    fo.write(df.loc[i][0])
    fo.write('\', value: ')
    fo.write(str(df.loc[i][1]))
    if i == len(df)-1:
        fo.write('}')
        break
    else:
        fo.write('},')
    fo.write('\n')

fo.close()

