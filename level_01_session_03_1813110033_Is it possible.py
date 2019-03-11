# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:42:49 2019

@author: Rajesh D Borate
"""

n=int(input())
arr=[]
arr = list(map(int, input().split()))
for i in range(n):
    if(arr[i]%2==0):
        print("YES")
    else:
        print("NO")