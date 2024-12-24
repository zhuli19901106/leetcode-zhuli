# medium
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/
# still a sliding window + count subarray problem
# but with some really whimsical bit manipulations
# hint, count bits, even or odd
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        mm = {0: 1}
        res = 0

        xor = 0
        for x in nums:
            xor ^= x
            res += mm[xor] if xor in mm else 0

            if not xor in mm:
                mm[xor] = 0
            mm[xor] += 1
        return res
