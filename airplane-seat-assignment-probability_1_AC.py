# https://leetcode.com/problems/airplane-seat-assignment-probability/
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp = 1.0
        for i in range(2, n + 1):
            dp = 1.0 / i + (i - 2.0) / i * dp
        return dp
