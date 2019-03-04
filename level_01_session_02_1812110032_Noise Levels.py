# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:44:54 2019

@author: Rajesh D Borate
"""

n=int(input())
if(n>=130):
    print("Jackhammer")
elif(n>=106 and n<=129):
    print("Gas lawnmower")
elif(n>=41 and n<=105):
    print("Alarm clock")
else:
    print("Quiet room")