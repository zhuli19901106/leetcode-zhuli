# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/
# 1AC, as you command

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        mm = defaultdict(int)
        p = head
        while p:
            mm[p.val] += 1
            p = p.next

        h1, t1 = None, None
        p = head
        while p:
            p1 = p.next
            p.next = None
            if mm[p.val] > 1:
                p = p1
                continue
            if h1:
                t1.next = p
                t1 = p
            else:
                h1 = t1 = p
            p = p1
        return h1
