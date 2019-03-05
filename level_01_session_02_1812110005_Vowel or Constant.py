# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:53:50 2019

@author: Rajesh D Borate
"""

s=input()
l=["a","e","i","o","u"]
if s in l:
    print("Vowel")
elif(s=='y'):
    print("Vowel or Consonant")
else:
    print("Consonant")