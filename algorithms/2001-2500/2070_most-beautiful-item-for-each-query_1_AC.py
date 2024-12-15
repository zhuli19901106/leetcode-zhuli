# https://leetcode.com/problems/most-beautiful-item-for-each-query/
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(items)

        pcs = [p for p, b in items]
        bts = []
        max_bt = 0
        for i in range(n):
            max_bt = max(max_bt, items[i][1])
            bts.append(max_bt)

        res = []
        for q in queries:
            i = bisect_right(pcs, q) - 1
            if i >= 0:
                res.append(bts[i])
            else:
                res.append(0)
        return res
