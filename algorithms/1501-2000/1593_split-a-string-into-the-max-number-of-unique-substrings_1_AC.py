# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
# BF search, without pruning
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = [1]
        st = set()
        self.dfs(s, 0, st, res)
        return res[0]

    def dfs(self, s, i, st, res):
        n = len(s)
        if i == n:
            res[0] = max(res[0], len(st))
            return

        for j in range(i, n):
            ss = s[i: j + 1]
            if ss in st:
                continue
            st.add(ss)
            self.dfs(s, j + 1, st, res)
            st.remove(ss)
