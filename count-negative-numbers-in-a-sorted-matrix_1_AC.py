# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# brute-force BFS
from collections import deque

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        a = grid
        q = deque()
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >=0 and y <= m - 1

        res = 0
        vst = set()

        q.append((n - 1, m - 1))
        while len(q) > 0:
            x, y = q.popleft()
            if x * m + y in vst:
                continue

            vst.add(x * m + y)
            if a[x][y] < 0:
                res += 1

            if inbound(x, y - 1):
                q.append((x, y - 1))
            if inbound(x - 1, y):
                q.append((x - 1, y))
        return res
