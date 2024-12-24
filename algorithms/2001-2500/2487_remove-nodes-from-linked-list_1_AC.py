# medium
# https://leetcode.com/problems/remove-nodes-from-linked-list/
# it's monotonic
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h0 = ListNode(0)
        h0.next = head
        st = [h0]

        p = head
        while p:
            st.append(p)
            p = p.next

        h1 = ListNode(0)
        max_val = 0
        while len(st) > 1:
            p = st.pop()
            prev = st[-1]
            if p.val < max_val:
                p.next = None
                prev.next = None
                continue

            # reverse insertion
            if h1:
                p.next = h1.next
                h1.next = p
            max_val = p.val
        p = h1
        h1 = h1.next
        p.next = None

        return h1
