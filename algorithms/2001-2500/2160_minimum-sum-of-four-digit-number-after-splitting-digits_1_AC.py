# easy
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution:
    def minimumSum(self, num: int) -> int:
        a = sorted(map(int, str(num)))
        return (a[0] * 10 + a[3]) + (a[1] * 10 + a[2])
