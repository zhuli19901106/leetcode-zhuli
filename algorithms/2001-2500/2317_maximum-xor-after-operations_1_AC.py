# medium
# https://leetcode.com/problems/maximum-xor-after-operations/
# total teaser
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res |= x

        return res
