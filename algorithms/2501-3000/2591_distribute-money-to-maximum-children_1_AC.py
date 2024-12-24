# easy
# https://leetcode.com/problems/distribute-money-to-maximum-children/
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money > 8 * children:
            return children - 1
        if money == 8 * (children - 1) + 4:
            return children - 2
        return (money - children) // 7
