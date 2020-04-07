# https://leetcode.com/problems/stepping-numbers/
# 1AC, precompute
from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self):
        step_nums = set()
        max_idx = 10

        def dfs(num, idx):
            step_nums.add(num)
            if idx == max_idx:
                return
            d = num % 10
            if d > 0:
                dfs(num * 10 + d - 1, idx + 1)
            if d < 9:
                dfs(num * 10 + d + 1, idx + 1)

        for i in range(10):
            dfs(i, 0)
        self.step_nums = sorted(step_nums)

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        step_nums = self.step_nums
        il = bisect_left(step_nums, low)
        ih = bisect_right(step_nums, high)
        return step_nums[il: ih]
