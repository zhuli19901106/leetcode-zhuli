# https://leetcode.com/problems/clone-n-ary-tree/
# 1AC

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        root1 = Node(root.val)
        root1.children = []

        if root.children is None:
            return root1

        for child in root.children:
            root1.children.append(self.cloneTree(child))
        return root1
