# medium
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
# brute-force

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            mm = {}
            j = i
            while j < n:
                c = s[j]
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1
                j += 1
                res += max(mm.values()) - min(mm.values())

        return res
