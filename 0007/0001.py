# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:23:40 2018

@author: queena
"""


import random
import string

length,count=16,200

ResultDic={}
Source=list(string.ascii_uppercase)

for index in range(0,10):
    Source.append(str(index))

while len(ResultDic)<count:
    key=''
    for index in range(0,length):
        key+=random.choice(Source)
    if key in ResultDic:
        pass
    else:
        ResultDic[key]=1
#    print(key)
    f=open('0001.txt','a')
    f.write(key+'\n')
    f.close()
        

