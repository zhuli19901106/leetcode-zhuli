# easy
# https://leetcode.com/problems/buy-two-chocolates/
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_val = prices[0] + prices[1]
        return money - min_val if min_val <= money else money
