# https://leetcode.com/problems/optimal-partition-of-string/
class Solution:
    def partitionString(self, s: str) -> int:
        st = set()
        res = 0

        i = 0
        n = len(s)
        while i < n:
            if s[i] in st:
                st = set()
                res += 1
            st.add(s[i])
            i += 1
        if len(st) > 0:
            res += 1

        return res
