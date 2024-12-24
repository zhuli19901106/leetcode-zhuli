# medium
# https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/
# 1AC, pure simulation

class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(nums)
        for t, i in queries:
            t %= (2* n)
            if t >= 0 and t < n:
                cur_len = n - t
                res.append(nums[i + t] if i < cur_len else -1)
            else:
                cur_len = t - n
                res.append(nums[i] if i < cur_len else -1)
        return res
