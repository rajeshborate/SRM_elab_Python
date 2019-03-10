# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 06:54:42 2019

@author: Rajesh D Borate
"""

n=int(input())
for i in range(n):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    if(a>1000):
    	print("{0:.6f}".format(a*b*0.9))
    else:
        print("{0:.6f}".format(a*b))