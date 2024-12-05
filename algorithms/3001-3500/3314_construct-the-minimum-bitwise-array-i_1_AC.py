# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
# really tricky
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if (x & 1) == 0:
                res.append(-1)
                continue
            res.append((x & x + 1) | (((x ^ x + 1) + 1) >> 2) - 1)
        return res
