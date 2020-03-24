# https://leetcode.com/problems/binary-tree-pruning/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(root):
            if root is None:
                return root
            root.left = prune(root.left)
            root.right = prune(root.right)
            if root.left is None and root.right is None and root.val == 0:
                return None
            return root

        return prune(root)
