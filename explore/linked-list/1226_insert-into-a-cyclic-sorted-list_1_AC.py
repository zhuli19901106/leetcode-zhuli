# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# 1AC, O(n) solution by locating head and inserting
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        p = Node(insertVal)
        p.next = p
        if head is None:
            return p

        h = head.next
        while h != head and h.val <= h.next.val:
            h = h.next
        h = h.next

        p1 = h
        while p1.next != h:
            if p1.val <= p.val and p.val <= p1.next.val:
                break
            else:
                p1 = p1.next
        p.next = p1.next
        p1.next = p
        return head
