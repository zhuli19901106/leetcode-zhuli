# https://leetcode.com/problems/next-greater-node-in-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        st = []
        m = {}
        ptr = head
        idx = 0
        while not ptr is None:
            while len(st) > 0 and ptr.val > st[-1][1]:
                m[st[-1][0]] = ptr.val
                st.pop()
            st.append((idx, ptr.val))
            ptr = ptr.next
            idx += 1

        n = idx
        res = [0 for i in range(n)]
        for k, v in m.items():
            res[k] = v
        return res
