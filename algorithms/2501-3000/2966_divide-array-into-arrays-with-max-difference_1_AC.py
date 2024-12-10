# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        m = len(nums) // 3
        for i in range(m):
            if abs(nums[3 * i + 2] - nums[3 * i]) > k:
                return []\

        res = []
        for i in range(m):
            res.append(nums[3 * i: 3 * (i + 1)])
        return res
