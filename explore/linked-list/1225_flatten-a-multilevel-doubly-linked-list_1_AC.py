# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# careful, don't be sloppy
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flattenRecur(head):
            if not head:
                return None, None
            p = h = t = head
            while p:
                t = p
                if p.child:
                    h1, t1 = flattenRecur(p.child)
                    p.child = None
                    tmp = p.next
                    p.next = h1
                    h1.prev = p
                    if tmp:
                        t1.next = tmp
                        tmp.prev = t1
                p = p.next
            return h, t

        h, _ = flattenRecur(head)
        return h
