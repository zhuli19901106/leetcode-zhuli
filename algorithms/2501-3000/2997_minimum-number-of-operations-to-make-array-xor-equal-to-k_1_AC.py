# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for x in nums:
            xor ^= x
        xor ^= k

        res = 0
        while xor != 0:
            xor &= xor - 1
            res += 1
        return res
