# easy
# https://leetcode.com/problems/finding-3-digit-even-numbers/
# 1AC, DFS

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ad = [0 for i in range(10)]
        for x in digits:
            ad[x] += 1
        st = set()
        self._dfs(st, 0, ad, 0)

        res = list(st)
        res.sort()
        return res

    def _dfs(self, st, cur, ad, idx):
        if idx == 3:
            st.add(cur)
            return

        for i in range(10):
            if ad[i] <= 0:
                continue
            if idx == 0 and i == 0:
                continue
            if idx == 2 and i % 2 == 1:
                continue
            ad[i] -= 1
            self._dfs(st, cur * 10 + i, ad, idx + 1)
            ad[i] += 1
