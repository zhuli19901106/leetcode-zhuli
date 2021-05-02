# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
# 1AC, bruteforce search, simple, slow and acceptable
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        st = set()
        sa = [int(_) for _ in s]
        self.dfs(sa, st, a, b)
        return sorted(st)[0]

    def dfs(self, sa, st, a, b):
        s = ''.join([str(_) for _ in sa])
        if s in st:
            return
        st.add(s)

        n = len(s)

        sa1 = sa[:]
        for i in range(1, n, 2):
            sa1[i] = (sa1[i] + a) % 10
        self.dfs(sa1, st, a, b)

        sa1 = sa[-b:] + sa[:-b]
        self.dfs(sa1, st, a, b)
