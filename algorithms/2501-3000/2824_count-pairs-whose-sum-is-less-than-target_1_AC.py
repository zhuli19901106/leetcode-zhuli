# easy
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        i, j = 0, n - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
                continue
            res += j - i
            i += 1
        return res
