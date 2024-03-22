# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sm1 = sum(nums)
        sm2 = 0
        for x in nums:
            while x != 0:
                sm2 += x % 10
                x //= 10

        return abs(sm1 - sm2)
