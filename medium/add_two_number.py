#!/usr/bin/env python
# coding=utf-8
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List 
        :type l2: List 
        :rtype: List 
        """
        s = self.convert(l1) + self.convert(l2)
        return self.toLinkedList(s)
    
    def convert(self,l):
        str_ = ""
        for i in l:
            str_ += str(i)
        return int(str_)
    
    def toLinkedList(self,s):
        return list(str(s))

if __name__ == "__main__":
    a = Solution()
    l1 = list(input("input first number:"))
    l2 = list(input("input secend number: "))
    print(a.addTwoNumbers(l1, l2))
