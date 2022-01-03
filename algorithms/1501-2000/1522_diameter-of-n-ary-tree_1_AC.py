# https://leetcode.com/problems/diameter-of-n-ary-tree/
# not quite a clean solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if root is None:
            return 0

        # calculate depth for nodes
        mdep = {}
        self.calcDepth(root, mdep)

        return self.calcDiameter(root, mdep)

    def calcDiameter(self, root, mdep):
        res = 0
        deps = []
        for child in root.children:
            if child is None:
                continue
            res = max(res, self.calcDiameter(child, mdep))
            deps.append(mdep[child])
        deps.sort()

        if len(deps) >= 1:
            res = max(res, deps[-1])
        if len(deps) >= 2:
            res = max(res, deps[-1] + deps[-2])

        return res

    def calcDepth(self, root, mdep):
        max_dep = 0
        for child in root.children:
            if child is None:
                continue
            dep = self.calcDepth(child, mdep)
            max_dep = max(max_dep, dep)
        mdep[root] = max_dep + 1

        return mdep[root]
