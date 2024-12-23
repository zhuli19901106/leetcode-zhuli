# https://leetcode.com/problems/count-the-number-of-good-subarrays/
# why do people like subarrays so much?
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mm = {}

        res = 0
        cp = 0
        j = 0
        for i, x in enumerate(nums):
            if not x in mm:
                mm[x] = 0

            cp += mm[x]
            mm[x] += 1

            # keep moving forward until it's not "good"
            while cp >= k:
                mm[nums[j]] -= 1
                cp -= mm[nums[j]]
                j += 1

            res += i - j + 1

        res = n * (n + 1) // 2 - res
        return res
