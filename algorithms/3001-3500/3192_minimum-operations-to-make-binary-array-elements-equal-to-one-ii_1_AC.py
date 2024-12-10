# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = []
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            a.append(nums[i])
            i = j

        i, j = 0, len(a) - 1
        res = 0
        if nums[i] == 1:
            i += 1
        if nums[j] == 0:
            j -= 1
            res += 1
        res += j - i + 1
        return res
