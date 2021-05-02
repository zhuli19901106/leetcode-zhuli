# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# 1AC, simple prefix and postfix counting
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        st = set()
        pre = [0 for _ in range(n)]
        for i in range(n):
            st.add(s[i])
            pre[i] = len(st)

        st.clear()
        post = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            st.add(s[i])
            post[i] = len(st)

        res = 0
        for i in range(n - 1):
            if pre[i] == post[i + 1]:
                res += 1
        return res
