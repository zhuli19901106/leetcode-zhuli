# https://leetcode.com/problems/minimum-number-game/
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = sorted(nums)
        n = len(res)
        for i in range(0, n, 2):
            res[i], res[i + 1] = res[i + 1], res[i]
        return res
