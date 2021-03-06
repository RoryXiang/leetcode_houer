"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
"""


def constructMaximumBinaryTree(arry):
    max_ = max(arry)
    node = Node()
    node.value = max_
    left_list = arry[:arry.index(max_)]
    left(left_list, node)
    right_list = arry[arry.index(max_) + 1:]
    right(right_list, node)
    return node


def left(arry, node_):
    if len(arry) == 0:
        return
    if len(arry) == 1:
        node = Node()
        node.value = arry[0]
        node_.left = node
        return
    node = Node()
    max_ = max(arry)
    node.value = max_
    node_.left = node
    left_list = arry[:arry.index(max_)]
    left(left_list, node)
    right_list = arry[arry.index(max_) + 1:]
    right(right_list, node)
    pass


def right(arry, node_):
    if len(arry) == 0:
        return
    if len(arry) == 1:
        node = Node()
        node.value = arry[0]
        node_.right = node
        return
    node = Node()
    max_ = max(arry)
    node.value = max_
    node_.right = node
    left_list = arry[:arry.index(max_)]
    left(left_list, node)
    right_list = arry[arry.index(max_) + 1:]
    right(right_list, node)


class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


if __name__ == '__main__':
    a = constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])

    print(a.right.value)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(root, low, high):
            max = -1000
            j = 0
            for i in range(low, high):
                if max < nums[i]:
                    max = nums[i]
                    j = i
            root.val = max
            if low < j:
                root.left = TreeNode(None)
                construct(root.left, low, j)
            if j + 1 < high:
                root.right = TreeNode(None)
                construct(root.right, j + 1, high)
        root = TreeNode(None)
        construct(root, 0, len(nums))
        return root


s = Solution()
print(s.constructMaximumBinaryTree([1, 2, 3]))
