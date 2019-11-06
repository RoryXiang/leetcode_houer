#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 11:03:14
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$

"""
1143 Longest Common Subsequence
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        matrix = [[0 for x in range(n) for _ in range(m)]]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]


if __name__ == '__main__':
    print(2222)
