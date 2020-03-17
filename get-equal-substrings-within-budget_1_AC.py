# https://leetcode.com/problems/get-equal-substrings-within-budget/
# 1AC, perfect, sliding window
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        a = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        res = 0
        i = j = 0
        cost = 0
        while i < n and j < n:
            while j < n and cost + a[j] <= maxCost:
                cost += a[j]
                j += 1
            res = max(res, j - i)
            if i < j:
                cost -= a[i]
                i += 1
            else:
                i += 1
                j = i
                cost = 0
        return res
