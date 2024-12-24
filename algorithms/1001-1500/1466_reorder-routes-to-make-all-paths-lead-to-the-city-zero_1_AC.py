# medium
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# 1AC, create an equivalent undirected graph
from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ug = defaultdict(lambda: set())
        edges = set([(x, y) for x, y in connections])
        for x, y in edges:
            ug[x].add(y)
            ug[y].add(x)

        q = deque()
        st = set()

        res = 0
        q.append(0)
        st.add(0)
        while len(q) > 0:
            x = q.popleft()
            for y in ug[x]:
                if y in st:
                    continue
                if not (y, x) in edges:
                    res += 1
                q.append(y)
                st.add(y)
        return res
