# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 6 == 0]
        return sum(a) // len(a) if len(a) > 0 else 0
