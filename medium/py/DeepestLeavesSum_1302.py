#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DeepestLeavesSum_1302.py
@Time    :   2020/09/15 22:19:36
@Author  :   RoryXiang 
@Version :   1.0
'''

"""
Given a binary tree, return the sum of values of its deepest leaves.
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Get to the deepest leave.
        # Check if there are more leaves with such depth.
        # Sum values.
        if not root:
            return 0
        
        # DFS, using a stack
        stack = [(root, 0)]
        leaves = [(0, 0)]
        max_lvl = 0
        max_sum = 0
        
        while stack:
            node, lvl = stack.pop()
            if node:
                if lvl > max_lvl:
                    max_lvl = lvl
                    max_sum = 0
                    
                if node.right:
                    stack.append((node.right, lvl+1))
                
                if node.left:
                    stack.append((node.left, lvl+1))
                
                if not node.right and not node.left and lvl == max_lvl:
                    # leave node
                    max_sum += node.val
        
        return max_sum