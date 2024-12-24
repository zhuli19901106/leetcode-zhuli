# medium
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Runtime: 384 ms, faster than 96.88% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
# Memory Usage: 62.9 MB, less than 100.00% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def traverse(root, d, zz):
            res = zz
            if root.left:
                z1 = traverse(root.left, 0, zz + 1 if d != 0 else 1)
                res = max(res, z1)
            if root.right:
                z2 = traverse(root.right, 1, zz + 1 if d != 1 else 1)
                res = max(res, z2)
            return res

        if root:
            return traverse(root, -1, 0)
        return 0
