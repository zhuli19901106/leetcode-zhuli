# medium
# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def check(root, arr, idx):
            if root is None or root.val != arr[idx]:
                return False
            if root.left is None and root.right is None:
                return idx == len(arr) - 1
            if idx == len(arr) - 1:
                return root.left is None and root.right is None
            return check(root.left, arr, idx + 1) or check(root.right, arr, idx + 1)

        return check(root, arr, 0)
