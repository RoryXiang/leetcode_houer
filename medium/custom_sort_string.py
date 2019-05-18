#!/usr/bin/env python
# coding=utf-8
"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
"""


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_list = list(S)
        t_list = list(T)
        out_list = []
        for one in s_list:
            if one in t_list:
                out_list.append(one)
                t_list.remove(one)
        out_list.extend(t_list)
        return "".join(out_list)
