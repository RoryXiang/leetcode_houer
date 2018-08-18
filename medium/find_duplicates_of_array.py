#!/usr/bin/env python
# coding=utf-8
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        once_dict = {}
        two_dict = {}
        more_dict = {}
        for item in nums:
            if once_dict.get(item):
                once_dict.pop(item)
                two_dict[item] = 2
                result.append(item)
            elif two_dict.get(item):
                two_dict.pop(item)
                result.remove(item)
                more_dict[item] = 3
            elif more_dict.get(item):
                more_dict[item] = more_dict[item] + 1
            else:
                once_dict[item] = 1
        return result
