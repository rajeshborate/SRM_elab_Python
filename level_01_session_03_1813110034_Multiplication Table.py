# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:55:35 2019

@author: Rajesh D Borate
"""

n=int(input())
a=int(input())

for i in range(1,a+1):
    print("{} * {} = {}".format(i,n,i*n))
    i+=1