# https://leetcode.com/problems/greatest-sum-divisible-by-three/
# sort of a brain teaser
# Runtime: 264 ms, faster than 90.18% of Python3 online submissions for Greatest Sum Divisible by Three.
# Memory Usage: 17.8 MB, less than 100.00% of Python3 online submissions for Greatest Sum Divisible by Three.
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_val = sum(nums)
        a = sorted([x for x in nums if x % 3 != 0])
        n = len(a)
        if sum_val % 3 == 0:
            return sum_val
        res = 0
        for i in range(n):
            if (sum_val - a[i]) % 3 == 0:
                res = max(res, sum_val - a[i])
                break

        i = 0
        while i < n:
            if (sum_val - a[i]) % 3 != 0:
                break
            i += 1
        j = i + 1
        while j < n:
            if (sum_val - a[i] - a[j]) % 3 == 0:
                break
            j += 1
        if i < n and j < n:
            res = max(res, sum_val - a[i] - a[j])

        return res
