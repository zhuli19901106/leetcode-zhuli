# https://leetcode.com/problems/jump-game-iii/
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        a = arr
        n = len(a)
        vs = [False for i in range(n)]

        q = deque()
        vs[start] = True
        q.append(start)
        while len(q) > 0:
            x = q.popleft()
            if a[x] == 0:
                return True
            for off in (-a[x], +a[x]):
                if x + off >= 0 and x + off <= n - 1 and not vs[x + off]:
                    vs[x + off] = True
                    q.append(x + off)
        return False
