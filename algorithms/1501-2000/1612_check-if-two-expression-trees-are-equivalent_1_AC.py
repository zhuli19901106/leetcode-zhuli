# medium
# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/
# 1AC, what's the point?

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        mm1 = defaultdict(int)
        self.traverse(root1, mm1)
        mm2 = defaultdict(int)
        self.traverse(root2, mm2)

        for k in mm1:
            if not k in mm2 or mm1[k] != mm2[k]:
                return False
        for k in mm2:
            if not k in mm1 or mm2[k] != mm1[k]:
                return False
        return True

    def traverse(self, root, mm):
        if root is None:
            return
        if root.left is None and root.right is None:
            mm[root.val] += 1

        if root.left:
            self.traverse(root.left, mm)
        if root.right:
            self.traverse(root.right, mm)
