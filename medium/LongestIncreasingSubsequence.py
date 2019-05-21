# -*- coding:UTF-8 -*-

"""[summary]
Given an unsorted array of integers, find the length of longest increasing subsequence.
解题思路： 将第1个数字加入解集；依次读取后面的数字，如果此数字比解集中最后一个数字大，则将此数字追加到解集后，否则，用这个数字替换解集中第一个比此数字大的数
参考链接： https://www.jianshu.com/p/a3cd9df6d9d1
"""


class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        rst = [nums[0]]
        for i in range(1, n):
            if nums[i] > rst[-1]:
                rst.append(nums[i])
            else:
                index = self.midSearch(rst, nums[i])
                rst[index] = nums[i]
        return len(rst)

    def midSearch(self, s, k):
        p = 0
        q = len(s) - 1
        while(p <= q):
            m = (p + q) // 2
            if s[m] == k:
                return m
            if s[m] > k:
                q = m - 1
            else:
                p = m + 1
        return p
