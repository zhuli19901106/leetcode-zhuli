# https://leetcode.com/problems/find-eventual-safe-states/
# careful with travesal states, more than just visited
class Solution:
    '''
    0 unvisited
    1 visited but unknown
    2 visited without cycle
    3 visited with cycle
    '''
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = graph
        n = len(g)
        safe = [0 for i in range(n)]
        
        def dfs(idx):
            nonlocal safe

            if safe[idx] == 1:
                safe[idx] = 3
                return
            if safe[idx] >= 2:
                return

            safe[idx] = 1
            cnt_cyc = 0
            for idx1 in g[idx]:
                dfs(idx1)
                if safe[idx1] == 3:
                    cnt_cyc += 1
            safe[idx] = 3 if cnt_cyc > 0 else 2

        for i in range(n):
            dfs(i)

        res = [i for i, x in enumerate(safe) if x == 2]
        return res
