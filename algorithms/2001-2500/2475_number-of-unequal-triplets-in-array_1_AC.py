# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == nums[i]:
                    continue
                for k in range(j + 1, n):
                    if nums[k] == nums[j] or nums[k] == nums[i]:
                        continue
                    res += 1

        return res
