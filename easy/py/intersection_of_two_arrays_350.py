#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   intersection_of_two_arrays_350.py
@Time    :   2020/09/01 15:04:42
@Author  :   RoryXiang 
@Version :   1.0
'''

'''
Given two arrays, write a function to compute their intersection.
'''


# here put the import lib

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = {}
        for num in nums1:
            temp[num] = temp.get(num, 0) + 1
        k = 0
        for num in nums2:
            if temp.get(num, 0) > 0:
                nums2[k] = num
                k += 1
                temp[num] = temp[num] - 1
        return nums2[:k]