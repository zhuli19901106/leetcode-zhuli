# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        sm = []
        q = deque()

        q.appendleft((root, 0))
        while len(q) > 0:
            r, lv = q.pop()
            if len(sm) <= lv:
                sm.append(0)
            sm[lv] += r.val

            if r.left:
                q.appendleft((r.left, lv + 1))
            if r.right:
                q.appendleft((r.right, lv + 1))
        sm.sort()

        return sm[len(sm) - k] if len(sm) >= k else -1
