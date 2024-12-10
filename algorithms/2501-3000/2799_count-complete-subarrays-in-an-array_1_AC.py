# https://leetcode.com/problems/count-complete-subarrays-in-an-array/
# sliding window
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uc = len(set(nums))
        n = len(nums)
        mm = {}

        res = 0
        j = 0
        for i in range(n):
            if not nums[i] in mm:
                mm[nums[i]] = 1
            else:
                mm[nums[i]] += 1

            if not len(mm) == uc:
                continue
            while j <= i and len(mm) == uc:
                mm[nums[j]] -= 1
                if mm[nums[j]] == 0:
                    del mm[nums[j]]
                j += 1
            res += j

            # key here
            j -= 1
            mm[nums[j]] = 1

        return res
