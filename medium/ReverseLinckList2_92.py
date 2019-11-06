#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-31 14:08:38
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$


"""
leetcode 92
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

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

    def solve(self, head, m, n):
        if m == n:
            return head

        first = None
        first_prev = None
        temp = None
        index = 1
        while index <= n:
            # print(index)
            if index <= m:
                if not first:
                    first = head
                else:
                    first_prev = first
                    first = first.next
                index += 1
                continue
            if not temp:
                temp = first.next
                temp_next = temp.next
                temp.next = first
                temp = temp_next
                temp_prev = first.next
            else:
                temp_next = temp.next
                temp.next = temp_prev
                temp_prev = temp
                temp = temp_next

            index += 1
        if not first_prev:
            head = temp_prev
        else:
            first_prev.next = temp_prev
        first.next = temp_next
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
    head = s.solve(head, 1, 2)
    print(1111)

    contenler = []
    while head:
        print(44444)
        contenler.append(head.value)
        head = head.next
        print(head)

    print(contenler)
