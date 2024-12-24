# medium
# https://leetcode.com/problems/split-bst/
# 1AC, recursive split
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        r1, r2 = None, None
        if root is None:
            return r1, r2
        if root.val <= V:
            r1 = root
            rr1, r2 = self.splitBST(root.right, V)
            r1.right = rr1
        else:
            r2 = root
            r1, rr2 = self.splitBST(root.left, V)
            r2.left = rr2
        return [r1, r2]
