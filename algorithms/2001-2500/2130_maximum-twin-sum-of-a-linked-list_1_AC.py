# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# why bother?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(h):
            if h is None:
                return h
            h1, t1 = None, None
            p = h
            while p:
                if h1 is None:
                    t1 = p
                p1 = p.next
                p.next = h1
                h1 = p

                p = p1
            return h1

        par, p1, p2 = None, head, head
        while p2:
            par = p1
            p1 = p1.next
            p2 = p2.next
            if p2 is None:
                break
            p2 = p2.next

        h1 = head
        h2 = par.next
        par.next = None
        h2 = reverseList(h2)

        res = -1
        p1, p2 = h1, h2
        while p1 and p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next

        return res
