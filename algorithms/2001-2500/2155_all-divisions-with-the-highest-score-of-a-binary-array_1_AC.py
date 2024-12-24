# medium
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1 = [0 for i in range(n)]
        sm = 0
        for i in range(n):
            c1[i] = sm + (1 - nums[i])
            sm = c1[i]

        c2 = [0 for i in range(n)]
        sm = 0
        for i in range(n - 1, -1, -1):
            c2[i] = sm + nums[i]
            sm = c2[i]

        max_val = 0
        for i in range(n + 1):
            v1 = c1[i - 1] if i > 0 else 0
            v2 = c2[i] if i < n else 0
            max_val = max(max_val, v1 + v2)
        res = []
        for i in range(n + 1):
            v1 = c1[i - 1] if i > 0 else 0
            v2 = c2[i] if i < n else 0
            if v1 + v2 == max_val:
                res.append(i)

        return res
