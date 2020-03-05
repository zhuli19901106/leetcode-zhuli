# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# 1AC, count as you go, sliding window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        m0 = {'a': 1, 'b': 1, 'c': 1}
        m = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)
        res = n * (n + 1) // 2
        cc = len(m0)

        j = 0
        for i, c in enumerate(s):
            m[c] += 1
            if m[c] == m0[c]:
                cc -= 1
            # all satisfied
            while cc == 0:
                m[s[j]] -= 1
                if m[s[j]] < m0[s[j]]:
                    cc += 1
                j += 1
            res -= i - j + 1
        return res
