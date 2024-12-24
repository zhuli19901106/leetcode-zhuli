# medium
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None or head.next is None:
            return [-1, -1]

        acp = []
        p1, p2 = head, head.next
        i = 1
        while p2.next:
            p3 = p2.next
            if (p2.val > p1.val and p2.val > p3.val) or \
                (p2.val < p1.val and p2.val < p3.val):
                acp.append(i)

            p1, p2 = p2, p3
            i += 1

        n = len(acp)
        if n < 2:
            return [-1, -1]
        min_dist = acp[1] - acp[0]
        max_dist = acp[n - 1] - acp[0]
        for i in range(1, n - 1):
            dist = acp[i + 1] - acp[i]
            min_dist = min(min_dist, dist)

        return [min_dist, max_dist]
