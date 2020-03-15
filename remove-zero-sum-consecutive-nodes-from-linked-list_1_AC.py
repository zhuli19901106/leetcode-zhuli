# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# my god... that's too sloppy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        INT_MAX = 2 ** 31 - 1
        def removeZeroList(head):
            if head is None:
                return head, False
            h = ListNode(0)
            h.next = head

            p = h
            idx = 0
            mm = {0: h}
            sum_val = 0
            while p.next:
                sum_val += p.next.val
                if sum_val in mm:
                    p1 = mm[sum_val]
                    p1.next = p.next.next
                    return h.next, True
                mm[sum_val] = p.next
                p = p.next
            return head, False

        # skip all 0 nodes
        h = ListNode(0)
        h.next = head
        p = h
        while p and p.next:
            if p.next.val == 0:
                p.next = p.next.next
            p = p.next

        h = h.next
        while True:
            h, suc = removeZeroList(h)
            if not suc:
                break
        return h
