#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   add_two.py
@Time    :   2021/06/07 23:45:14
@Author  :   RoryXiang 
@Version :   1.0
'''

# here put the import lib
from typing import List


def add(nums: List[int], target: int):
    tmp = {}
    for index, value in enumerate(nums):
        # print(tmp, target - value, tmp.get(target-value))
        if tmp.get(target - value) is not None:
            return (index, tmp.get(target - value))
        else:
            tmp[value] = index
    print(tmp)


a = [2, 7, 12, 13]

m = add(a, 9)
print(m)
