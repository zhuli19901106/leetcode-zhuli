# medium
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
# just search it
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        a = []
        st = set()
        
        res = self.dfs(1, a, st, n, k)
        return res

    def dfs(self, x, a, st, n, k):
        if len(a) == n:
            return sum(a)

        a.append(x)
        st.add(x)
        y = x + 1
        while True:
            if k - y in st:
                y += 1
                continue

            ret = self.dfs(y, a, st, n, k)
            if ret != -1:
                return ret

            y += 1
        st.remove(x)
        a.pop()

        return -1
