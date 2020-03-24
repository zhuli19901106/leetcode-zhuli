# https://leetcode.com/problems/armstrong-number/
# 1AC
class Solution:
    def isArmstrong(self, N: int) -> bool:
        ps = 0
        sn = str(N)
        k = len(sn)
        for c in sn:
            ps += (ord(c) - ord('0')) ** k
        return ps == N
