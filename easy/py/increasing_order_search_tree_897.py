"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
the root of the tree, and every node has no left child and only one right child.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def increasingBST(root: TreeNode) -> TreeNode:
    def inorder(rt: Optional[TreeNode], node: TreeNode) -> TreeNode:
        if rt is not None:
            node = inorder(rt.left, node)

            node.right = TreeNode(val=rt.val)
            node = node.right

            node = inorder(rt.right, node)
        return node
    tmp_node = TreeNode()
    inorder(root, tmp_node)
    return tmp_node.right


if __name__ == "__main__":
    a = TreeNode(5)
    a.left = TreeNode(1)
    a.left.left = TreeNode(2)
    a.left.right = TreeNode(3)
    a.right = TreeNode(7)
    a.right.left = TreeNode(8)
    a.right.right = TreeNode(9)
    tmp = TreeNode()
    ff = increasingBST(a)
    print(ff.val, "=====")

    pp = increasingBST(a)

    node1 = pp
    while node1 is not None:
        print(node1.val)
        node1 = node1.right
