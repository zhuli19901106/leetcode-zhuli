# medium
# https://leetcode.com/problems/minimum-knight-moves/
# 1AC, standard BFS with reasonable pruning
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        tx, ty = x, y

        offs = []
        for x in (-2, +2):
            for y in (-1, +1):
                offs.append((x, y))
                offs.append((y, x))
        
        # pruning here
        thres = 5

        res = {}
        q = deque()

        res[(0, 0)] = 0
        q.append((0, 0))
        while not (tx, ty) in res:
            x, y = q.popleft()
            d = res[(x, y)]
            dx = abs(x - tx)
            dy = abs(y - ty)
            for off in offs:
                if dx > thres and off[0] * (tx - x) < 0:
                    continue
                if dy > thres and off[1] * (ty - y) < 0:
                    continue
                x1, y1 = x + off[0], y + off[1]
                if (x1, y1) in res:
                    continue
                res[(x1, y1)] = d + 1
                q.append((x1, y1))
        return res[(tx, ty)]
