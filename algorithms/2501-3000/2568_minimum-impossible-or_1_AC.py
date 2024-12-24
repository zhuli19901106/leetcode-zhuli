# medium
# https://leetcode.com/problems/minimum-impossible-or/
# must be a teaser, it is indeed
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for x in nums:
            if x > res + 1:
                break
            res |= x
        res += 1

        return res
