# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:49:01 2022

edited on 3 nov for ajay

@author: sahil
"""


nums = [2,7,11,15,20]
target = 9

#---------------------------------------------------------------
# Solution 1
my_dict = {}

# Solution needed : nums(a) + nums(b) = Target
# Solution exploited : nums(b) = Target - nums(a)

for i, j  in enumerate(nums):
    
    # Uses dictionry/Map. All keys are possible values
    
    if (target - j) in my_dict :
        print(i,my_dict[target - j] )
    
    else :
        my_dict[j] = i

#---------------------------------------------------------------

# Solution 2
temp_nums = nums
nums = sorted(nums)

# Use two pointers, starting on either side. If sum is greater than target, reduce right hand side
# If sum is lesser than target, increase left pointer

left = 0
right = len(nums) - 1

while left != right:
    
    if nums[left] + nums[right] == target:
        index_1 = temp_nums.index(nums[left])
        temp_nums[index_1] = "considered"
        index_2 = temp_nums.index(nums[right])
        print(index_1, index_2)
        break
        
    elif nums[left] + nums[right] < target:
        left += 1
        
    elif nums[left] + nums[right] > target:
        right -= 1
      