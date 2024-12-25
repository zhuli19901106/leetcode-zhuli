# hard
# https://leetcode.com/problems/subarrays-with-k-different-integers/
# think about it, exactly, at most
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - \
            self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums, k):
        if k == 0:
            return 0

        n = len(nums)
        mm = {}

        res = 0
        j = 0
        for i, x in enumerate(nums):
            if not x in mm:
                mm[x] = 0
            mm[x] += 1

            while len(mm) > k:
                y = nums[j]
                mm[y] -= 1
                if mm[y] == 0:
                    del mm[y]
                j += 1
            res += i - j + 1

        return res
