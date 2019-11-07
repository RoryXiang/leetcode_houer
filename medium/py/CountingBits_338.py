#!/usr/bin/env python
# coding=utf-8
"""
Given a non negative integer number num. For every numbers i in the
range 0 ≤ i ≤ num calculate the number of 1's in their binary representation
and return them as an array.
"""
import math


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        out_list = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            out_list[i] = self.get_num(i)
        return out_list

    def get_num(self, num, out=0):
        if int(math.log(num, 2)) == math.log(num, 2):
            return out + 1
        else:
            num = num - 2**(int(math.log(num, 2)))
            out += 1
            return self.get_num(num, out=out)


if __name__ == "__main__":
    a = Solution()
    b = a.countBits(5)
    print(a.get_num(99))
    print(b)
