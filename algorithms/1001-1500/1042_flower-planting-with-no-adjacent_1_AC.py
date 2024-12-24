# medium
# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# I know it's not hard, but easy?
# A bit overworked, right?
# Too slow.
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        n = N
        adj = [[] for i in range(n)]
        for x, y in paths:
            adj[x - 1].append(y - 1)
            adj[y - 1].append(x - 1)
        visited = {}

        def dfs(idx, adj, visited):
            nexts = []
            n = len(adj)
            for x in adj[idx]:
                if not x in visited:
                    nexts.append(x)
            while len(nexts) > 0:
                x = nexts.pop()
                cols = set()
                for x1 in adj[x]:
                    if x1 in visited:
                        cols.add(visited[x1])
                for i in range(1, n + 1):
                    if not i in cols:
                        break
                visited[x] = i
                if dfs(x, adj, visited):
                    break

        while len(visited) != n:
            for idx in range(n):
                if not idx in visited:
                    break
            visited[idx] = 1
            dfs(idx, adj, visited)
        res = [0 for i in range(n)]
        for k, v in visited.items():
            res[k] = v
        return res
