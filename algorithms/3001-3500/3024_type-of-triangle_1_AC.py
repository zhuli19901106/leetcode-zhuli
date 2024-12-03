# https://leetcode.com/problems/type-of-triangle/
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a == b and b == c:
            return 'equilateral'
        if a + b <= c:
            return 'none'
        if a == b or b == c:
            return 'isosceles'
        return 'scalene'
