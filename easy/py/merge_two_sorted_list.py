# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# add auth store test by zhangxianbiao

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = cursor = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                cursor.next, l1 = l1, l1.next
            else:
                cursor.next, l2 = l2, l2.next
            cursor = cursor.next
            
        cursor.next = l1 or l2
        return result.next
