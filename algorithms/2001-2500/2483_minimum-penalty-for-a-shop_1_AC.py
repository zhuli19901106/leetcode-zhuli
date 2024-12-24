# medium
# https://leetcode.com/problems/minimum-penalty-for-a-shop/
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cy, cn = 0, 0
        for c in customers:
            if c == 'Y':
                cy += 1
            else:
                cn += 1

        pen = cy
        min_pen, min_i = pen, 0
        for i, c in enumerate(customers):
            if c == 'Y':
                cy -= 1
                pen -= 1
            else:
                cn -= 1
                pen += 1
            if pen < min_pen:
                min_pen, min_i = pen, i + 1
        return min_i
