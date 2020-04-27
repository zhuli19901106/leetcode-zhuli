# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3308/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= n - 1
        return n
