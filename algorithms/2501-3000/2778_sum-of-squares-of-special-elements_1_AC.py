# easy
# https://leetcode.com/problems/sum-of-squares-of-special-elements/
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([x * x for i, x in enumerate(nums) if len(nums) % (i + 1) == 0])
