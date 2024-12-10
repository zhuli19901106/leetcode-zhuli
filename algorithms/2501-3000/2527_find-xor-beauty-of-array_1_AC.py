# https://leetcode.com/problems/find-xor-beauty-of-array/
# this is ridiculous, wild guess
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res
