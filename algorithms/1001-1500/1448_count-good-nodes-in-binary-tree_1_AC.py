# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# 1AC, no hurry
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(root, max_val):
            cur = 0
            if root.val >= max_val:
                cur += 1
            max_val = max(max_val, root.val)
            left = dfs(root.left, max_val) if root.left else 0
            right = dfs(root.right, max_val) if root.right else 0
            return cur + left + right

        return dfs(root, root.val)
