# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(root, val, arr):
            if root.left is None and root.right is None:
                arr.append((val << 1) | root.val)
                return
            if not root.left is None:
                traverse(root.left, (val<< 1) | root.val, arr)
            if not root.right is None:
                traverse(root.right, (val<< 1) | root.val, arr)

        arr = []
        traverse(root, 0, arr)
        return sum(arr)
