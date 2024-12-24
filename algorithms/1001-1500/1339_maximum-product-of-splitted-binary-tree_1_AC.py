# medium
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# cut a subtree from it
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        if root is None:
            return 0
        MOD = 10 ** 9 + 7

        def treeSum(root, mm):
            if root is None:
                return 0
            mm[root] = root.val + treeSum(root.left, mm) + treeSum(root.right, mm)
            return mm[root]

        mm = {}
        total = treeSum(root, mm)
        res = 0
        for ptr, val in mm.items():
            if ptr == root:
                continue
            res = max(res, val * (total - val))

        return res % MOD
