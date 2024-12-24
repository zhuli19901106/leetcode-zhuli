# medium
# https://leetcode.com/problems/possible-bipartition/
# 1AC, BFS
from collections import deque

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        n = N
        g = [set() for i in range(n)]
        for x, y in dislikes:
            g[x -  1].add(y - 1)
            g[y - 1].add(x - 1)

        res = [-1 for i in range(n)]
        suc = True
        for i in range(n):
            if not suc:
                break
            if res[i] != -1:
                continue

            q = deque()
            res[i] = 0
            q.append(i)
            while len(q) > 0 and suc:
                j = q.popleft()
                for j1 in g[j]:
                    if res[j1] == 1 - res[j]:
                        continue
                    if res[j1] == res[j]:
                        suc = False
                        break
                    if res[j1] == -1:
                        res[j1] = 1 - res[j]
                        q.append(j1)
        return suc
