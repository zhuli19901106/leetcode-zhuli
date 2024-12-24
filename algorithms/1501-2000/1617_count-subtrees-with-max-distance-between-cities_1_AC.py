# hard
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
# so everybody is going straight for BF?
from collections import deque

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(g, x0):
            mm = {}
            q = deque()

            max_x, max_val = x0, 0
            mm[x0] = 0
            q.append((x0, 0))
            while len(q) > 0:
                x, val = q.popleft()
                if val > max_val:
                    max_x, max_val = x, val

                if not x in g:
                    continue
                for y in g[x]:
                    if y in mm:
                        continue
                    mm[y] = val + 1
                    q.append((y, val + 1))

            return max_x, max_val, mm

        def verify(cur_edges):
            n = len(cur_edges)
            if n == 0:
                return False, 0

            g = {}
            for x, y in cur_edges:
                if not x in g:
                    g[x] = set()
                if not y in g:
                    g[y] = set()
                g[x].add(y)
                g[y].add(x)
            for x in g:
                x0 = x
                break

            nv = len(g)
            if nv != n + 1:
                return False, 0

            max_x, max_val, mm = bfs(g, x0)
            if len(mm) != nv:
                return False, 0

            x0 = max_x
            max_x, max_val, mm = bfs(g, x0)

            return True, max_val

        ne = len(edges)
        res = [0 for i in range(ne)]
        for bm in range(1 << ne):
            cur_edges = []
            for i in range(ne):
                if (bm & (1 << i)) != 0:
                    cur_edges.append(edges[i])

            is_tree, max_rad = verify(cur_edges)

            if not is_tree:
                continue
            res[max_rad - 1] += 1

        return res
