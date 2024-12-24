# easy
# https://leetcode.com/problems/maximum-strong-pair-xor-i/
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) > min(nums[i], nums[j]):
                    continue
                res = max(res, nums[i] ^ nums[j])
        return res
