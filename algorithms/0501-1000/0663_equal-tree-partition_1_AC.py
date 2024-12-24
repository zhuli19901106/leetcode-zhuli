# medium
# https://leetcode.com/problems/equal-tree-partition/
# 1AC, subtree sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        if root is None:
            return False

        def calcSum(root):
            if root is None:
                return 0
            return calcSum(root.left) + root.val + calcSum(root.right)

        total_sum = calcSum(root)
        found = False

        def traverse(root):
            nonlocal found

            if root is None:
                return 0

            ls = traverse(root.left)
            if root.left and ls == total_sum - ls:
                found = True
            rs = traverse(root.right)
            if root.right and rs == total_sum - rs:
                found = True
            sm = ls + root.val + rs
            return sm

        traverse(root)
        return found
