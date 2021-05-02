# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# 1AC, don't even bother with that unnerving and geeky pointer operations
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        for i in range(k - 1):
            if p1 is None:
                break
            p1 = p1.next
        if p1 is None:
            return head

        p2, pt = head, p1.next
        while pt:
            p2, pt = p2.next, pt.next
        p1.val, p2.val = p2.val, p1.val
        return head
