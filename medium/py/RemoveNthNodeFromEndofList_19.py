#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-04 15:36:29
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$

"""
leetcode 19
Remove Nth Node From End of List
"""


class Node(object):

    def __init__(self, x):
        self.value = x
        self.next = None


def Linck(a: list):
    head = None
    prev = None

    for i in a:
        if not head:
            node = Node(i)
            head = node
        else:
            prev = node
            node = Node(i)
            prev.next = node
    return head


class Solution(object):

    def solve(self, head, n):
        temp = head
        target_prev = None
        index = 0
        while temp:
            if index == n:
                target_prev = head
            if index > n:
                target_prev = target_prev.next
            temp = temp.next
            index += 1
            pass
        if index < n:
            return None
        elif index == n:
            return head.next
        else:
            target_prev.next = target_prev.next.next if target_prev.next.next else None
        return head


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    # a = [5]
    a = [3, 5]
    # a = [1, 2, 3]
    # a = [1, 2, 3, 4]
    head = Linck(a)

    s = Solution()
    # head = s.solve(head, 2, 4)
    head = s.solve(head, 1)
    # print(1111)

    contenler = []
    while head:
        # print(44444)
        contenler.append(head.value)
        head = head.next
        # print(head)

    print(contenler)
