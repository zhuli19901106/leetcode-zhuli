# medium
# https://leetcode.com/problems/inorder-successor-in-bst-ii/
# case by case, many cases
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
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        while True:
            if node is None:
                return None
            elif node.right:
                p = node.right
                while p.left:
                    p = p.left
                return p
            elif node.parent is None:
                return None
            elif node.parent.left == node:
                return node.parent
            else:
                while node.parent and node.parent.right == node:
                    node = node.parent
                return node.parent
