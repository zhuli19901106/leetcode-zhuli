# medium
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# bug free, please, not so sloppy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        last = False
        while len(q) > 0:
            ptr = q.popleft()
            if ptr is None:
                last = True
                continue
            if last:
                return False
            q.append(ptr.left)
            q.append(ptr.right)
        return True
