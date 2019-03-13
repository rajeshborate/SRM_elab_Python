# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:50:16 2019

@author: Rajesh D Borate
"""



# To take input from the user
lower = int(input())
upper = int(input())

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)