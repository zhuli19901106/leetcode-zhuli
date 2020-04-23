# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/
# 1AC
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def traverse(root, dp):
            nonlocal res

            if root is None:
                return dp - 1
            dpl = traverse(root.left, dp + 1)
            dpr = traverse(root.right, dp + 1)
            res = max(res, (dpl - dp) + (dpr - dp))

            return max(dpl, dpr)

        traverse(root, 0)
        return res
