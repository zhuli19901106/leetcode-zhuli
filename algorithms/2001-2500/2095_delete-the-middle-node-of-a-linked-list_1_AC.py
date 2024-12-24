# medium
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        par = None
        p1, p2 = head, head
        while p2:
            p2 = p2.next
            if p2 is None:
                break
            p2 = p2.next
            par = p1
            p1 = p1.next

        p1 = par.next
        par.next = p1.next if p1 else None
        del p1

        return head
