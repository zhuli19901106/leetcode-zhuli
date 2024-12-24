# medium
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum = {}
        Solution.traverse(root, 1, level_sum)
        min_level, max_sum = None, None
        for k, v in level_sum.items():
            if max_sum is None or max_sum < v or min_level > k:
                min_level, max_sum = k, v
        return min_level

    @staticmethod
    def traverse(root, level, level_sum):
        if not level in level_sum:
            level_sum[level] = 0
        level_sum[level] += root.val
        if not root.left is None:
            Solution.traverse(root.left, level + 1, level_sum)
        if not root.right is None:
            Solution.traverse(root.right, level + 1, level_sum)
