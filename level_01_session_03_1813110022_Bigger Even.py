# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:45:54 2019

@author: Rajesh D Borate
"""

n=int(input())
arr=[]
arr=list(map(int, input().split()))

arr.sort(reverse=True)
#print(arr)

a=len(arr)
#print (a)

for i in range(n):
    if(arr[i]%2==0):
        print("Largest even number:",arr[i])
        break
    else:
        continue