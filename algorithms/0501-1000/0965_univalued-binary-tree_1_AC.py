# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        m = set()
        self.traverse(root, m)
        return len(m) == 1

    def traverse(self, root, m):
        if root is None:
            return
        m.add(root.val)
        self.traverse(root.left, m)
        self.traverse(root.right, m)
