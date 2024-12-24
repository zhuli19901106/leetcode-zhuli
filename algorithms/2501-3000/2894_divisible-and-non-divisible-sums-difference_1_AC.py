# easy
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sm = n * (n + 1) // 2
        num2 = (n // m) * (n // m + 1) // 2 * m
        num1 = sm - num2
        return num1 - num2
