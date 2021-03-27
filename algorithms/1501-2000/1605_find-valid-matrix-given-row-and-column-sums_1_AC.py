# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
# 1AC, I got stuck for about 10 minutes before coming to my senses
from heapq import heappush, heappop

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        hr = []
        for i, x in enumerate(rowSum):
            heappush(hr, (x, i))

        m = len(colSum)
        hc = []
        for i, x in enumerate(colSum):
            heappush(hc, (x, i))

        res = [[0 for j in range(m)] for i in range(n)]
        while len(hr) > 0 and len(hc) > 0:
            rx, ri = heappop(hr)
            cx, ci = heappop(hc)
            val = min(rx, cx)
            res[ri][ci] += val
            if rx > val:
                heappush(hr, (rx - val, ri))
            if cx > val:
                heappush(hc, (cx - val, ci))
        return res
