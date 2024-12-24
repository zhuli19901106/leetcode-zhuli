# medium
# https://leetcode.com/problems/find-root-of-n-ary-tree/
# 1AC, disjoint set

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        dj = {}
        mn = {}
        for node in tree:
            mn[node.val] = node
            dj[node.val] = node.val

        def djRoot(x):
            r = x
            while r != dj[r]:
                r = dj[r]
            k = x
            while x != r:
                x = dj[x]
                dj[k] = r
                k = x
            return r

        for node in tree:
            x = node.val
            for child in node.children:
                y = child.val
                rx, ry = djRoot(x), djRoot(y)
                dj[ry] = rx
        for x in dj:
            return mn[djRoot(x)]
