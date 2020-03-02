# https://leetcode.com/problems/linked-list-components/
# union-find set
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        def findRoot(ds, x):
            if not x in ds:
                ds[x] = x
            r = x
            while r != ds[r]:
                r = ds[r]
            k = x
            while x != r:
                x = ds[x]
                ds[k] = r
                k = x
            return r
        
        ds = {}
        gs = set(G)
        last = None
        ptr = head
        while not ptr is None:
            if ptr.val in gs:
                findRoot(ds, ptr.val)
            if (not last is None) and (ptr.val in gs)\
                and (last.val in gs):
                r1 = findRoot(ds, ptr.val)
                r2 = findRoot(ds, last.val)
                ds[r1] = r2
            last = ptr
            ptr = ptr.next
        rs = {}
        for k in ds:
            v = findRoot(ds, k)
            if v in rs:
                rs[v] += 1
            else:
                rs[v] = 1
        return len(rs)
