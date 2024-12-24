# easy
# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
# 1AC, steady

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        rh = ListNode()
        rt = rh
        p = head
        while True:
            i = 0
            while i < m and p:
                rt.next = p
                p = p.next
                rt = rt.next
                rt.next = None
                i += 1
            if not p:
                break

            i = 0
            while i < n and p:
                p = p.next
                i += 1
            if not p:
                break

        rt = rh.next
        rh.next = None
        return rt
