# https://leetcode.com/problems/largest-substring-between-two-equal-characters/
# totally boring
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        m1, m2 = {}, {}
        for i in range(n):
            if not s[i] in m1:
                m1[s[i]] = i
        for i in range(n - 1, -1, -1):
            if not s[i] in m2:
                m2[s[i]] = i
        res = -1
        for k in m1.keys():
            if m1[k] == m2[k]:
                continue
            res = max(res, m2[k] - m1[k] - 1)
        return res
