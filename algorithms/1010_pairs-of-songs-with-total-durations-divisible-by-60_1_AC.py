# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = {}
        MOD = 60
        res = 0
        for x in time:
            x %= MOD
            y = (MOD - x) % MOD
            if y in m:
                res += m[y]
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        return res
