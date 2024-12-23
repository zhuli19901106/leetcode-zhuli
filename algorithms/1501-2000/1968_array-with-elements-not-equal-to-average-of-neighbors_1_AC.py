# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
# just try it at the end, no fancy tricks
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 2:
            return nums[:]

        nums.sort()
        res = nums[:2]
        i = 2
        while i < n:
            if nums[i] - res[-1] != res[-1] - res[-2]:
                res.append(nums[i])
                i += 1
                continue

            j = i
            while j >= 2 and 2 * res[j - 1] == nums[i] + res[j - 2]:
                j -= 1
            res.insert(j, nums[i])
            i += 1
        return res
