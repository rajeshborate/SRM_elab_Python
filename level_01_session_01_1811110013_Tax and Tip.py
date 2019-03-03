# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 06:32:09 2019

@author: Rajesh D Borate
"""

a=int(input())
tax=0.05*a
tip=0.18*a
print("The tax is {0:.2f} and the tip is {1:.1f} making the total {2:.2f}".format(tax,tip,tax+tip+a))
