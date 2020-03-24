# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(root, arr):
            if root is None:
                return
            traverse(root.left, arr)
            arr.append(root)
            traverse(root.right, arr)

        arr = []
        traverse(root, arr)
        n = len(arr)
        for i in range(n - 1, 0, -1):
            arr[i - 1].val += arr[i].val
        return root
