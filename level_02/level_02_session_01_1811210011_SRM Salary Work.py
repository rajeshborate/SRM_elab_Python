# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 06:56:20 2019

@author: Rajesh D Borate
"""

n=int(input())
for i in range(n):
    basic=int(input())
    if(basic<1500):
        hra=0.1*basic
        da=0.9*basic
        sal=hra+da+basic
        print(sal)
    else:
        hra=500
        da=0.98*basic
        sal=hra+da+basic
        print(sal)
        