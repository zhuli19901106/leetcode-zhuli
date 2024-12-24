# easy
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def traverse(root, arr):
            if root is None:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)

        arr = []
        traverse(root, arr)
        n = len(arr)
        res = arr[1] - arr[0]
        for i in range(1, n - 1):
            res = min(res, arr[i + 1] - arr[i])
        return res
