# easy
# https://leetcode.com/problems/find-if-digit-game-can-be-won/
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sm1 = sum([x for x in nums if x >= 1 and x <= 9])
        sm2 = sum(nums) - sm1
        return sm1 != sm2
