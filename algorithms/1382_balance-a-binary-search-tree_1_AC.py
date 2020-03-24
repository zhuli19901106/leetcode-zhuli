# https://leetcode.com/problems/balance-a-binary-search-tree/
# 1AC, I'll settle for the simple and intuitive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(root, arr):
            if root is None:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)

        def constructBalanced(arr, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = constructBalanced(arr, left, mid - 1)
            root.right = constructBalanced(arr, mid + 1, right)
            return root

        arr = []
        traverse(root, arr)
        root1 = constructBalanced(arr, 0, len(arr) - 1)
        return root1
