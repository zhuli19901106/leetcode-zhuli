# https://leetcode.com/problems/delete-leaves-with-a-given-value/
# 1AC
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def isleaf(root):
            return root.left is None and root.right is None

        def deleteNode(root, target):
            if not root.left is None:
                root.left = deleteNode(root.left, target)
            if not root.right is None:
                root.right = deleteNode(root.right, target)
            if isleaf(root) and root.val == target:
                return None
            return root

        if root is None:
            return None
        root = deleteNode(root, target)
        return root
