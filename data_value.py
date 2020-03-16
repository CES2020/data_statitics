#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yaoli 
@file: data_value.py 
@time: 2020/03/16 
"""

import pandas as pd
import numpy as np

df = pd.read_csv('place_2.csv')
df = pd.DataFrame(df)
a = df.drop_duplicates()
# print(df.info())
# print(a.info())
a.to_csv('place_dup.csv', index=False, header=False)

## 统计
df['value'] = 1

result = df.groupby('name')['value'].sum().sort_values(ascending=False)
result_json = result.to_json(force_ascii=False, orient='table')
fo = open('name_value.json', 'r+')
fo.write(result_json)
#print(result_json)
