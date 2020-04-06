# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
# always use caching for brute-force DFS
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for i in range(n):
            g[i] = set()
        for x, y in edges:
            g[x].add(y)

        def dfs(x, path, vst):
            if x in path:
                # cycle detected
                return False

            if x in vst:
                # key optimization
                return True
            res = True
            if len(g[x]) == 0:
                if x == destination:
                    vst.add(x)
                    return True
                else:
                    return False

            path.add(x)
            for y in g[x]:
                if not dfs(y, path, vst):
                    return False
            vst.add(x)
            path.remove(x)
            return res

        return dfs(source, set(), set()):
