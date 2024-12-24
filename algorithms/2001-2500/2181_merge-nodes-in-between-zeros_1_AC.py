# medium
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        h1, t1 = None, None
        while p and p.next:
            cur_sm = 0
            p1 = p.next
            while p1 and p1.val != 0:
                cur_sm += p1.val
                p1 = p1.next
            p = p1

            if cur_sm == 0:
                continue

            if h1:
                t1.next = ListNode(cur_sm)
                t1 = t1.next
            else:
                h1 = ListNode(cur_sm)
                t1 = h1

        return h1
