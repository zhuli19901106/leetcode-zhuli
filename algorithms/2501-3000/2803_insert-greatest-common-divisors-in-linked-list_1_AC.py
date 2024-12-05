# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        while p1 and p1.next:
            p2 = p1.next
            p3 = ListNode(val=self.gcd(p1.val, p2.val))

            p3.next = p2
            p1.next = p3
            p1 = p2
        return head

    def gcd(self, x, y):
        if x > y:
            x, y = y, x
        while x != 0:
            x, y = y % x, x
        return y
