# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:42:47 2019

@author: Rajesh D Borate
"""

n=int(input())
sum=0
if(n>0):
    for i in range(1,n+1):
        sum=sum+i
    print("The sum is",sum)
else:
    print("Enter a positive number")
      
