# easy
# https://leetcode.com/problems/number-of-arithmetic-triplets/
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        st = set(nums)

        res = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] + diff in st and nums[i] + 2 * diff in st:
                res += 1
        return res
