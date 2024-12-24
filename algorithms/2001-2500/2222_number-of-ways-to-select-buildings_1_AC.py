# medium
# https://leetcode.com/problems/number-of-ways-to-select-buildings/
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)

        p0, p1 = [], []
        for i in range(n):
            if s[i] == '0':
                p0.append(i)
            else:
                p1.append(i)

        res = 0
        res += self.check(s, p0, p1, '0', '1')
        res += self.check(s, p1, p0, '1', '0')
        return res

    def check(self, s, p1, p2, c1, c2):
        n = len(s)

        res = 0
        ll, rr = 0, len(p1)
        for i in range(n):
            if s[i] == c1:
                ll += 1
                rr -= 1
            else:
                res += ll * rr
        return res
