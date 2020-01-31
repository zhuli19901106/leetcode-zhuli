# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorderTraverse(root, arr)
        n = len(arr)
        for i in range(n - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]
        arr[n - 1].left = None
        arr[n - 1].right = None
        return arr[0]

    def inorderTraverse(self, root, arr):
        if root is None:
            return
        self.inorderTraverse(root.left, arr)
        arr.append(root)
        self.inorderTraverse(root.right, arr)
