# medium
# https://leetcode.com/problems/brace-expansion/
# 1AC, DFS
class Solution:
    def expand(self, S: str) -> List[str]:
        s = S
        n = len(s)
        a = []
        i = 0
        while i < n:
            if s[i] != '{':
                a.append(s[i])
                i += 1
                continue
            j = s.find('}', i)
            a.append(sorted(s[i + 1: j].split(',')))
            i = j + 1

        res = []

        def dfs(idx, sa):
            nonlocal res

            if idx == len(a):
                res.append(''.join(sa))
                return
            if isinstance(a[idx], str):
                sa.append(a[idx])
                dfs(idx + 1, sa)
                sa.pop()
            else:
                for c in a[idx]:
                    sa.append(c)
                    dfs(idx + 1, sa)
                    sa.pop()

        dfs(0, [])
        return res
