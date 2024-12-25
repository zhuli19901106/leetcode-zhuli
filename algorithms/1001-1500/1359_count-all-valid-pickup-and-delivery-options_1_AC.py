# hard
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
# how is this hard?
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = int(1e9 + 7)

        res = 1
        for i in range(2, n + 1):
            res = res * ((2 * i - 1) * i) % MOD
        return res
