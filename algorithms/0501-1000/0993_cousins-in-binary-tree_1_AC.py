# easy
# https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        par = {}
        depth = {}
        def traverse(root, d):
            if root is None:
                return
            depth[root.val] = d
            if root.left != None:
                par[root.left.val] = root.val
                traverse(root.left, d + 1)
            if root.right != None:
                par[root.right.val] = root.val
                traverse(root.right, d + 1)

        traverse(root, 0)
        return depth[x] == depth[y] and par[x] != par[y]
