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
# a = df.drop_duplicates()
# print(df.info())
# print(a.info())
# a.to_csv('place_dup.csv', index=False, header=False)

## 统计
## df['value'] = 1
## 发现点太小导致数据结果不明显，准备乘10
df['value'] = 1

## 用 gropuby 来统计重复项
result = df.groupby('name')['value'].sum().sort_values(ascending=False)
result = pd.DataFrame(result)
result.reset_index(inplace=True)
## 转 json  这种官方方法确实能转，但是无法输出回车键，不美观，不如自己大力出奇迹写个循环
# result_json = result.to_json(force_ascii=False, orient='table')
fo = open('name_value.txt', 'r+')
fdp = open('place_dup.csv', 'r+')
# fo.write(result_json)
fo.truncate(0)
fdp.truncate(0)

for i in range(len(result)):
    fo.write('{name: \'')
    fo.write(result.loc[i][0])
    fdp.write(result.loc[i][0])
    fo.write('\', value: ')
    fo.write(str(result.loc[i][1]))
    if i == len(result)-1:
        fo.write('}')
        break
    else:
        fo.write('},')
    fo.write('\n')
    fdp.write('\n')

fo.close()
fdp.close()
