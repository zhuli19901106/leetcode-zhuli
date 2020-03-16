# https://leetcode.com/problems/distant-barcodes/
# finally, got this one clear after multiple wrong ideas
# duplicate of # https://leetcode.com/problems/reorganize-string/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        mm = {}
        for x in barcodes:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        a = list(mm.items())
        a.sort(key=lambda x: -x[1])
        na = len(a)

        k = a[0][0]
        h = Node(k)
        p = h
        for i in range(a[0][1] - 1):
            p.next = Node(k)
            p = p.next
        p = h
        for i in range(1, na):
            k, v = a[i]
            for j in range(v):
                while not p or p.val == k:
                    if not p:
                        p = h
                    else:
                        p = p.next
                p1 = Node(k)
                p1.next = p.next
                p.next = p1
                p = p.next.next

        res = []
        p = h
        while p:
            res.append(p.val)
            p = p.next
        return res
