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


class Solution_(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while(fast != slow):
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    a = Solution_()
    b = a.findDuplicates([1, 2, 3, 4, 5, 6, 7, 4])
    print(b)
