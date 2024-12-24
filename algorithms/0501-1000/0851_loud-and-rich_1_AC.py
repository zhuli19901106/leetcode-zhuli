# medium
# https://leetcode.com/problems/loud-and-rich/
# memorized search, but quite the work to write it down
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [set() for i in range(n)]
        for x, y in richer:
            graph[y].add(x)

        child = {}

        def dfs(x):
            nonlocal graph, child

            if x in child:
                return child[x]
            cx = set()
            for y in graph[x]:
                cx.add(y)
                cy = dfs(y)
                cx |= cy
            child[x] = cx
            return cx

        for i in range(n):
            dfs(i)
        for i in range(n):
            child[i].add(i)
        res = []
        for i in range(n):
            a = list(child[i])
            a.sort(key=lambda x: quiet[x])
            res.append(a[0])
        return res
