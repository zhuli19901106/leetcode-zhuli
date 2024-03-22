# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        val = num
        while val > 0:
            d = val % 10
            val //= 10
            if num % d == 0:
                res += 1

        return res
