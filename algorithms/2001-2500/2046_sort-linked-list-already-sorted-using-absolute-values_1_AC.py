# https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/
# 1AC, easy does it

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # positive
        h1, t1 = None, None
        # negative
        h2, t2 = None, None

        p = head
        while p:
            p1 = p.next
            p.next = None

            if p.val >= 0:
                if h1 is None:
                    h1 = t1 = p
                else:
                    t1.next = p
                    t1 = p
            else:
                if h2 is None:
                    h2 = t2 = p
                else:
                    p.next = h2
                    h2 = p
            p = p1
        if h1 is None:
            return h2
        elif h2 is None:
            return h1
        else:
            t2.next = h1
            return h2
