# easy
# https://leetcode.com/problems/matrix-cells-in-distance-order/class Solution:
from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        offsets = [[-1, 0], [+1, 0], [0, -1], [0, +1]]

        def inbound(x, y):
            return x >= 0 and x <= R - 1 and y >= 0 and y <= C - 1

        q = deque()
        b = [[False for j in range(C)] for i in range(R)]
        q.append((r0, c0))
        res = []
        while len(q) > 0:
            x, y = q.popleft()
            if b[x][y]:
                continue 
            b[x][y] = True
            res.append([x, y])
            for off in offsets:
                x1 = x + off[0]
                y1 = y + off[1]
                if inbound(x1, y1) and not b[x1][y1]:
                    q.append((x1, y1))
        return res
