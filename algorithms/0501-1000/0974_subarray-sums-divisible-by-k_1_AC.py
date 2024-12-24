# medium
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        a = [x % K for x in A]
        ds = {0: 1}
        ps = 0
        res = 0
        for x in a:
            ps = (ps + x) % K
            if ps in ds:
                res += ds[ps]
                ds[ps] += 1
            else:
                ds[ps] = 1
        return res
