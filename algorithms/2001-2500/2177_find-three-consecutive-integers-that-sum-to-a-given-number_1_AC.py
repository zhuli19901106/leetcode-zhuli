# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
# this is absurd

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            x = num // 3
            return [x - 1, x, x + 1]
        else:
            return []
