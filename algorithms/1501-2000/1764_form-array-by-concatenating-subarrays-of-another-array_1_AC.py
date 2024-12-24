# medium
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
# what? subsequence of subarrays?
# bruteforce match
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        m = len(groups)
        i, j = 0, 0
        while i < n and j < m:
            g = groups[j]
            ng = len(g)

            ki, kj = i, 0
            while ki < n and kj < ng:
                if nums[ki] != g[kj]:
                    break
                ki += 1
                kj += 1
            if kj == ng:
                i += ng
                j += 1
            else:
                i += 1

        return j == m
