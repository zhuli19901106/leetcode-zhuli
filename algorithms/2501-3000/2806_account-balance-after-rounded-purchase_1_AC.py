# easy
# https://leetcode.com/problems/account-balance-after-rounded-purchase/
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        pa = purchaseAmount
        if pa % 10 >= 5:
            pa += 10
        pa = pa // 10 * 10
        return 100 - pa
