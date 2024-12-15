# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
# is this really necessary?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        h0 = ListNode(None)
        h0.next = head

        p = h0.next
        last_h, last_t = h0, h0
        k = 1
        while p:
            cc = 1

            cur_h, cur_t = p, p
            for i in range(k - 1):
                if p.next is None:
                    break
                p = p.next
                cur_t = p
                cc += 1

            # careful with the order
            p = cur_t.next
            cur_t.next = None
            k += 1

            if cc % 2 == 0:
                self.reverseList(cur_h)
                cur_h, cur_t = cur_t, cur_h

            last_t.next = cur_h
            last_h, last_t = cur_h, cur_t

        return h0.next

    def reverseList(self, head):
        if head is None:
            return head
        
        h = None
        p = head
        while p:
            p1 = p.next
            p.next = h
            h = p
            p = p1
        return h
