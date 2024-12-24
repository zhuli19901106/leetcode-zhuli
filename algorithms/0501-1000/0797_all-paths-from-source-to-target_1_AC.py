# medium
# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, path, visited, idx, target, res):
            if idx == target:
                res.append(path[:])
                return
            for x in graph[idx]:
                if x == idx:
                    continue
                if x in visited:
                    continue
                path.append(x)
                visited.add(x)
                dfs(graph, path, visited, x, target, res)
                visited.remove(x)
                path.pop()

        res = []
        path = []
        visited = set()
        n = len(graph)

        path.append(0)
        visited.add(0)
        dfs(graph, path, visited, 0, n - 1, res)
        visited.remove(0)
        path.pop()

        return res
