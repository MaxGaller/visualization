# -*- coding:utf-8 _*-
"""
@Author : wzy
@File   : data0.py
@Email  : 474770370@qq.com
"""
import pandas as pd

path = 'data.csv'
with open(path)as file:
    data = pd.read_csv(file)
    print(data.loc[:,'name'])
