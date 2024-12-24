# medium
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return Solution.equiv(root1, root2)
    
    @staticmethod
    def equiv(r1, r2):
        if r1 is None:
            return r2 is None
        elif r2 is None:
            return False
        if r1.val != r2.val:
            return False
        return (Solution.equiv(r1.left, r2.left) and Solution.equiv(r1.right, r2.right))\
            or (Solution.equiv(r1.left, r2.right) and Solution.equiv(r1.right, r2.left))
