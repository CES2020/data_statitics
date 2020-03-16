#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: data_value.py 
@time: 2020/03/16 
"""


import pandas as pd
import numpy as np

df = pd.read_csv('place_2.csv')
df['人次'] = 1
a = df.drop_duplicates()
print(df.info())
print(a.info())

