#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   group_people_1282.py
@Time    :   2020/09/01 16:13:57
@Author  :   RoryXiang 
@Version :   1.0
'''

"""
There are n people, each of them has a unique ID from 0 to n - 1 and each person of them belongs to exactly one group.

Given an integer array groupSizes which indicated that the person with ID = i belongs to a group of groupSize[i] persons.

Return an array of the groups where ans[j] contains the IDs of the jth group. Each ID should belong to exactly one group and each ID should be present in your answer. Also if a person with ID = i belongs to group j in your answer, then ans[j].length == groupSize[i] should be true.
"""

# here put the import lib

class Solution:
    def groupThePeople(self, groupSizes: [int]) -> [[int]]:
        temp = {}
        for index, size in enumerate(groupSizes):
            if not temp.get(size, []):
                temp[size] = [index]
            else:
                temp[size].append(index)

        result = []
        for size, peoples in temp.items():
            while size < len(peoples):
                result.append(peoples[:size])
                peoples = peoples[size:]
            result.append(peoples)
        return result

    def groupThePeople1(self, groupSizes: [int]) -> [[int]]:
        temp = {}
        for index, size in enumerate(groupSizes):
            if not temp.get(size, []):
                temp[size] = [index]
            else:
                temp[size].append(index)


        output = []
        for x in temp:
            output.extend(temp[x][i:i+x] for i in range(0, len(temp[x]), x))
        return output


if __name__ == "__main__":
    s = Solution()
    m = s.groupThePeople1([3,3,3,3,3,1,3])
    print(m)