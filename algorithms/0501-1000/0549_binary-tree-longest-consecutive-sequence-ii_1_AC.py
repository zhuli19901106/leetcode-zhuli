# medium
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# 1AC, intuitive recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(\
            self.longestConsecutive(root.left),\
            self.longestConsecutive(root.right),\
            self.traverse(root, -1) + self.traverse(root, +1) - 1)

    def traverse(self, root, dt):
        if root is None:
            return 0
        res = 1
        if root.left and root.left.val + dt == root.val:
            res = max(res, 1 + self.traverse(root.left, dt))
        if root.right and root.right.val + dt == root.val:
            res = max(res, 1 + self.traverse(root.right, dt))
        return res
