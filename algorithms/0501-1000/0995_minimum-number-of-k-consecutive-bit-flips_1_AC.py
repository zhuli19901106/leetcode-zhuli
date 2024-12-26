# hard
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
# sort of tricky, be greedy
from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()

        res = 0
        f = 0
        for i in range(n):
            if len(q) > 0 and i >= q[-1] + k:
                f = 1 - f
                q.pop()

            if f:
                nums[i] = 1 - nums[i]

            if nums[i] != 1 and i + k <= n:
                nums[i] = 1 - nums[i]
                res += 1

                f = 1 - f
                q.appendleft(i)

        for x in nums:
            if x == 0:
                return -1
        return res
