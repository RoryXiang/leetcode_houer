#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-31 17:20:10
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$

"""
leetcode 24
Swap Nodes in Pairs
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
    def solve(self, head):
        thead = Node(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b = c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    head = Linck(a)
