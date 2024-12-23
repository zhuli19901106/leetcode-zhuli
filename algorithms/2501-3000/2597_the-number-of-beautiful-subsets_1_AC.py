# https://leetcode.com/problems/the-number-of-beautiful-subsets/
# just BF
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mm = {}
        res = [-1]
        self.dfs(0, k, nums, mm, res)
        return res[0]

    def dfs(self, idx, k, nums, mm, res):
        if idx == len(nums):
            res[0] += 1
            return

        self.dfs(idx + 1, k, nums, mm, res)

        x = nums[idx]
        if x + k in mm or x - k in mm:
            return

        if not x in mm:
            mm[x] = 1
        else:
            mm[x] += 1

        self.dfs(idx + 1, k, nums, mm, res)

        if mm[x] == 1:
            del mm[x]
        else:
            mm[x] -= 1
