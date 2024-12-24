# medium
# https://leetcode.com/problems/count-beautiful-substrings-i/
# just BF with O(n^2) effort
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vw = set('aeiou')

        n = len(s)
        res = 0
        for i in range(n):
            vc = 0
            for j in range(i, n):
                if s[j] in vw:
                    vc += 1
                if vc == j - i + 1 - vc and vc * vc % k == 0:
                    res += 1
        return res
