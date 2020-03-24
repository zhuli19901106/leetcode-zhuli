# https://leetcode.com/problems/create-target-array-in-the-given-order/
# singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        def insert(h, v, i):
            p = Node(v)
            if h is None:
                return p
            if i <= 0:
                p.next = h
                return p
            pp = h
            while i > 1:
                pp = pp.next
                i -= 1
            p.next = pp.next
            pp.next = p
            return h

        h = None
        n = len(nums)
        for i in range(n):
            h = insert(h, nums[i], index[i])

        res = []
        p = h
        while p:
            res.append(p.val)
            p = p.next
        return res
