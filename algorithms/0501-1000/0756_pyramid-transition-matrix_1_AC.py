# medium
# https://leetcode.com/problems/pyramid-transition-matrix/
# 1AC, DFS
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        a = [['' for j in range(n - i)] for i in range(n)]
        for i in range(n):
            a[0][i] = bottom[i]
        m = {}
        for al in allowed:
            k = al[:2]
            v = al[2]
            if not k in m:
                m[k] = set()
            m[k].add(v)

        def dfs(x, y):
            if x >= n:
                return True
            s = a[x - 1][y] + a[x - 1][y + 1]
            if not s in m:
                return False
            for c in m[s]:
                if y > 0:
                    s1 = a[x][y - 1] + c
                    if not s1 in m:
                        continue
                a[x][y] = c
                if x + y == n - 1:
                    ret = dfs(x + 1, 0)
                else:
                    ret = dfs(x, y + 1)
                if ret:
                    return True
                a[x][y] = ''
            return False

        return dfs(1, 0)
