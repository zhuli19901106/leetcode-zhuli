# https://leetcode.com/problems/maximum-binary-tree-ii/
# 1AC
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        ptr_new = TreeNode(val)
        if root is None:
            return ptr_new
        if val > root.val:
            ptr_new.left = root
            return ptr_new

        ptr = root
        while (not ptr.right is None) and ptr.right.val > val:
            ptr = ptr.right
        if ptr.right is None:
            ptr.right = ptr_new
        else:
            ptr_new.left = ptr.right
            ptr.right = ptr_new
        return root
