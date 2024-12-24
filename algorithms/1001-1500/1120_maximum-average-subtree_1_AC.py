# medium
# https://leetcode.com/problems/maximum-average-subtree/
# 1AC, post order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = -(2 ** 31 - 1)

        def traverse(root):
            nonlocal res

            if root is None:
                return 0, 0
            ls, lc = traverse(root.left)
            rs, rc = traverse(root.right)
            sm = ls + rs + root.val
            cnt = lc + rc + 1
            res = max(res, sm / cnt)

            return sm, cnt

        traverse(root)
        return res
