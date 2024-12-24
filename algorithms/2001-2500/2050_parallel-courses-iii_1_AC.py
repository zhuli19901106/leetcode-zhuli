# hard
# https://leetcode.com/problems/parallel-courses-iii/
# still topological, but with a max time condition
from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        ind = [0 for i in range(n)]
        g = {}
        for x, y in relations:
            # 1-indexed
            x -= 1
            y -= 1
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            
            # there may be repeated edges
            if not y in g[x]:
                g[x].add(y)
                ind[y] += 1

        q = deque()
        res = {}
        for i in range(n):
            if ind[i] == 0:
                res[i] = time[i]
                q.appendleft((time[i], i))

        while len(q) > 0:
            d, x = q.pop()

            if not x in g:
                continue

            for y in g[x]:
                if ind[y] == 0:
                    continue

                if (not y in res) or (res[y] < res[x] + time[y]):
                    res[y] = res[x] + time[y]

                ind[y] -= 1
                if ind[y] == 0:
                    q.appendleft((res[y], y))

        if len(res) != n:
            # contains cycle
            return -1
        return max(res.values())
