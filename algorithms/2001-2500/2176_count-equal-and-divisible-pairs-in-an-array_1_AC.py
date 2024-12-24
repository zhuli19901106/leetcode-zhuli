# easy
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# brute force

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    res += 1
        return res
