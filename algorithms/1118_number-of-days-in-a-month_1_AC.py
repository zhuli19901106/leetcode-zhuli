# https://leetcode.com/problems/number-of-days-in-a-month/
# 1AC
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if M != 2:
            return md[M]
        if Y % 400 == 0 or (Y % 100 != 0 and Y % 4 == 0):
            return md[M] + 1
        return md[M]
