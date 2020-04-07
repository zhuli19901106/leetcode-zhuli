# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# 1AC, remainder cycle
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        k = K
        if k == 1:
            return 1
        ak = [0 for i in range(k)]

        ak[1] = 1
        cur = 1
        cc = 1
        mod = 1
        while cur != 0:
            mod = mod * 10 % k
            cur = (cur + mod) % k
            cc += 1
            if cur == 0:
                return cc
            if ak[cur] != 0:
                return -1
            ak[cur] = cc
        return -1
