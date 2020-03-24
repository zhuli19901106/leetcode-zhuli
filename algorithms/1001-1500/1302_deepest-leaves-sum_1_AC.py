# https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.max_depth = 0
        
        arr = []
        self.traverse(root, arr, 0)
        return sum(arr)

    def traverse(self, root, arr, depth):
        if root is None:
            return
        if depth > self.max_depth:
            self.max_depth = depth
            arr.clear()
        if depth == self.max_depth:
            arr.append(root.val)
        self.traverse(root.left, arr, depth + 1)
        self.traverse(root.right, arr, depth + 1)
