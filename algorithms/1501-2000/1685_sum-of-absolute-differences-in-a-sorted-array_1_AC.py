# medium
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
# 1AC, careful with the indices
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ap = [0]
        cur = 0
        for x in nums:
            cur += x
            ap.append(cur)

        n = len(nums)
        res = [0 for _ in range(n)]
        for i, x in enumerate(nums):
            res[i] += i * x - ap[i + 1]
            res[i] += ap[n] - ap[i] - (n - i - 1) * x
        return res
