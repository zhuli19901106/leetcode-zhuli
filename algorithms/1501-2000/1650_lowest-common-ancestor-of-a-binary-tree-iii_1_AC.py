# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# 1AC, all the way up

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        dp = self.getDepth(p)
        dq = self.getDepth(q)
        while dp > dq:
            p = p.parent
            dp -= 1
        while dq > dp:
            q = q.parent
            dq -= 1
        while p is not None and p != q:
            p = p.parent
            q = q.parent
        return p

    def getDepth(self, node):
        tmp = node
        res = 0
        while tmp is not None:
            tmp = tmp.parent
            res += 1
        return res
