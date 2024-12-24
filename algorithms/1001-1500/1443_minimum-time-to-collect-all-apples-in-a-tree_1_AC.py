# medium
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
# 1AC, every edge involved is visited exactly twice

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            g[x].add(y)
            if not y in g:
                g[y] = set()
            g[y].add(x)

        def traverse(x, visited, apple_edges):
            visited.add(x)
            cx = 1 if hasApple[x] else 0

            for y in g[x]:
                if y in visited:
                    continue
                cy = traverse(y, visited, apple_edges)
                if cy > 0:
                    apple_edges.append((x, y))
                cx += cy

            return cx

        visited = set()
        apple_edges = []
        traverse(0, visited, apple_edges)

        res = 2 * len(apple_edges)

        return res

