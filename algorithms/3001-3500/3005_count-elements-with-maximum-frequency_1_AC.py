# easy
# https://leetcode.com/problems/count-elements-with-maximum-frequency/
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if not x in mm:
                mm[x] = 1
            else:
                mm[x] += 1
        maxf = max(mm.values())

        maxc = 0
        for k, v in mm.items():
            if v == maxf:
                maxc += 1
        return maxf * maxc
