# https://leetcode.com/problems/powerful-integers/
from collections import deque

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        q = deque()
        res = set()
        q.append((1, 1))
        while len(q) > 0:
            ex, ey = q.popleft()
            if ex + ey > bound:
                continue
            res.add(ex + ey)
            if x != 1:
                q.append((ex * x, ey))
            if y != 1:
                q.append((ex, ey * y))
        res = list(res)
        return res
