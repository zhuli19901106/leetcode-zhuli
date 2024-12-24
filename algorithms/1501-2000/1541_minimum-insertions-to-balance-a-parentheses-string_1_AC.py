# medium
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# be greedy
class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        cc = 0

        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                cc += 1
                i += 1
                continue

            if i == n - 1 or s[i + 1] == '(':
                # miss one ')'
                i -= 1
                res += 1

            if cc == 0:
                res += 1
            else:
                cc -= 1
            i += 2
        res += cc * 2

        return res
