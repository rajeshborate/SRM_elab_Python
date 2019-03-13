# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:52:15 2019

@author: Rajesh D Borate
"""

n=int(input())
a=int(input())
b=int(input())

arr=[int(input()) for i in range(n)]
#print(arr)
count,flag=0,0
for j in range(n):
    if((arr[j])>=a and (arr[j])<=b):
        count+=1
    else:
        flag+=1
if(flag==0):
    print("YES")
else:
    print("NO")
