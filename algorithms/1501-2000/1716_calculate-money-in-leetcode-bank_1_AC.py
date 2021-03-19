# https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# that's awkward...
class Solution:
    def totalMoney(self, n: int) -> int:
        nw = n // 7
        return 28 * nw + 7 * nw * (nw - 1) // 2 + (2 * nw + 1 + n % 7) * (n % 7) // 2
