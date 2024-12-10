# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        st = set(nums)
        h = ListNode(None, head)
        p = h
        while p.next:
            if p.next.val in st:
                p1 = p.next
                p.next = p1.next
            else:
                p = p.next
        return h.next
