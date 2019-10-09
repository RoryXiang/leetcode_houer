#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 19:22:12
# @Author  : RoryXiang (xiangshangping@lvwan.com)
# @Link    : ${link}
# @Version : $Id$


"""其实可以写一个排序，然后循环，做i, i+1, i+2和的计算找到最接近的三个数
"""


def three_sum_closest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]

    diff = target - res if target > res else res - target
    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, r = i + 1, len(nums) - 1

        largest = nums[i] + nums[r - 1] + nums[r]
        smallest = nums[i] + nums[left] + nums[left + 1]

        if largest <= target:
            # compare with the largest
            if largest == target:
                return largest

            if target - largest < diff:
                res = largest
                diff = target - largest
            continue

        elif smallest >= target:
            # compare with the smallest
            if smallest == target:
                return smallest

            if smallest - target < diff:
                res = smallest
                diff = smallest - target
            continue

        else:
            while left < r:
                s = nums[i] + nums[left] + nums[r]

                if s == target:
                    return s
                elif s < target:
                    left += 1
                    if target - s < diff:
                        res = s
                        diff = target - s
                else:
                    r -= 1
                    if s - target < diff:
                        res = s
                        diff = s - target
    return res


a = three_sum_closest([1, 2, 3, 4, 5, 5], 10)
print(a)
