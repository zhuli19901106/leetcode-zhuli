# medium
# https://leetcode.com/problems/merge-in-between-linked-lists/
# 1AC, just be careful
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = list1
        if a == 0:
            h1 = list2

        par1, cur1 = ListNode(val=0, next=list1), list1
        for i in range(a):
            par1 = par1.next
            cur1 = cur1.next

        par2, cur2 = par1, cur1
        for i in range(b - a + 1):
            par2 = par2.next
            cur2 = cur2.next

        h2 = list2
        t2 = h2
        while t2.next:
            t2 = t2.next

        par1.next = h2
        t2.next = cur2
        par2.next = None
        return h1
