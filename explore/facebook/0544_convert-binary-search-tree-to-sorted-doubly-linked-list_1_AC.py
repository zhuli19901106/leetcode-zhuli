# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# 1AC, perfect
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def traverse(root):
            if root is None:
                return None
            head = tail = root

            lh = traverse(root.left)
            if lh:
                lt = lh.left
                lt.right = root
                root.left = lt
                head = lh

            rh = traverse(root.right)
            if rh:
                rt = rh.left
                rh.left = root
                root.right = rh
                tail = rt

            head.left = tail
            tail.right = head
            return head

        return traverse(root)
