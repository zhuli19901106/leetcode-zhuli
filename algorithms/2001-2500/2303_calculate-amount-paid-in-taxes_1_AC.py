# easy
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        if income == 0:
            return tax

        last_up = 0
        for up, perc in brackets:
            cur = min(up, income) - last_up
            tax += cur * perc / 100.0
            last_up = up
            if income <= up:
                break

        return tax
