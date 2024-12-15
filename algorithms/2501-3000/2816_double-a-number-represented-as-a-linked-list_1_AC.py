# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# either reverse the list to save space, or use an array to save time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        head = self.reverseList(head)

        p = head
        while p:
            p.val *= 2
            p = p.next

        p = head
        while p:
            p1 = p.next

            c = p.val // 10
            p.val %= 10

            if c > 0:
                if p1:
                    p1.val += c
                else:
                    p1 = ListNode(c)
                    p.next = p1
                    break

            p = p1

        head = self.reverseList(head)
        return head

    def reverseList(self, head):
        h = None
        p = head
        while p:
            p1 = p.next
            p.next = h
            h = p

            p = p1
        return h
