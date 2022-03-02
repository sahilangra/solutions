# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:44:17 2022

@author: sahil
"""

s = "dvdf"
        
s = list(s)

pointer_1 = 0

temp = ""

while pointer_1 != len(s) - 1:

    pointer_2 = pointer_1 + 1

    while pointer_2 != len(s) + 1 :
        #print(pointer_1, "-", pointer_2)


        if len(s[pointer_1 : pointer_2]) == len(set(s[pointer_1 : pointer_2])) and (len(s[pointer_1 : pointer_2]) > len(temp)):
            temp = "".join(s[pointer_1 : pointer_2]) 


        pointer_2 += 1

    pointer_1 += 1
    
print( len(temp))