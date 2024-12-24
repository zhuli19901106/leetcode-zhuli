# medium
# https://leetcode.com/problems/count-number-of-homogenous-substrings/
# should be easy
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 1e9 + 7

        n = len(s)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            k = j - i
            res = (res + k * (k + 1) // 2) % MOD

            i = j
        
        res = int(res)
        return res
