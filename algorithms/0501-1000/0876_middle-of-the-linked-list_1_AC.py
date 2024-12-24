# easy
# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
        return p1
