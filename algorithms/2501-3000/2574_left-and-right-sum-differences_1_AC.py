# easy
# https://leetcode.com/problems/left-and-right-sum-differences/
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sl = [0 for _ in range(n)]
        sr = [0 for _ in range(n)]

        sm = 0
        for i in range(n):
            sl[i] = sm
            sm += nums[i]

        sm = 0
        for i in range(n - 1, -1, -1):
            sr[i] = sm
            sm += nums[i]

        res = []
        for i in range(n):
            res.append(abs(sl[i] - sr[i]))
        return res
