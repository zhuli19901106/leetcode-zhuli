# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0

        def traverse(root):
            nonlocal res

            if root is None:
                return 0
            root.val -= traverse(root.left)
            root.val -= traverse(root.right)
            # quite crafty, actually...
            res += abs(1 - root.val)
            return 1 - root.val

        traverse(root)
        return res
