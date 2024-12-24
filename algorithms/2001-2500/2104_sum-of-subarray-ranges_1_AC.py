# medium
# https://leetcode.com/problems/sum-of-subarray-ranges/
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        a = nums
        n = len(a)
        for i in range(n):
            min_val, max_val = a[i], a[i]
            for j in range(i + 1, n):
                min_val = min(min_val, a[j])
                max_val = max(max_val, a[j])
                res += max_val - min_val

        return res
