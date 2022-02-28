# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 23:10:35 2022

@author: sahil
"""

l1_list = [9,9,9,9,9,9,9]
l2_list = [9,9,9,9]

if len(l1_list) != len(l2_list):
    
    difference = abs(len(l1_list) - len(l2_list))
    
    if len(l1_list) > len(l2_list):
        l2_list.extend([0] * difference)
    elif len(l1_list) < len(l2_list):
        l1_list.extend([0] * difference)



carry = 0
count = 0
output_ = []

for i, j in zip(l1_list, l2_list):
    
    
    count += 1
    element = i + j + carry
    
    if carry:
        carry = 0
    
    if element >= 10:
        carry = element // 10
        element = element % 10

        
    output_.append(element)
    
    if count == len(l1_list):
        output_.append( carry)
        print("here")
        break
    