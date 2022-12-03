# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1
        else:
            ll = self.evaluateTree(root.left)
            rr = self.evaluateTree(root.right)
            return (ll or rr) if root.val == 2 else (ll and rr)
