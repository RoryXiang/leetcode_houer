#!/usr/bin/env python
# coding=utf-8
class MapSum(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))




class MapSum_():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dict[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        num = 0
        for key in self.dict:
            n = len(prefix)
            is_ok = True
            for i in range(n):
                try:
                    if key[i] == prefix[i]:
                        continue
                    else:
                        is_ok = False
                        break
                except:
                    is_ok = False
                    break
            if is_ok:
                num += self.dict[key]
        return num
        
