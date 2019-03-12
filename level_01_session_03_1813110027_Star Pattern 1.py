# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:45:00 2019

@author: Rajesh D Borate
"""

n=int(input())
for i in range(0, n):
    for j in range(n, i, -1):
        print("*", end="")
    print()