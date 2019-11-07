#!/usr/bin/env python
# coding=utf-8
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, num in enumerate(nums):
            if target <= num:
                return index
            else:
                continue
        return len(nums)
