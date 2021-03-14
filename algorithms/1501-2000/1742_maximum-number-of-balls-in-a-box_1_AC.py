# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
# 1AC
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mm = {}
        res = 0
        for x in range(lowLimit, highLimit + 1):
            sm = self.getDigitSum(x)
            if sm in mm:
                mm[sm] += 1
            else:
                mm[sm] = 1
            if mm[sm] > res:
                res = mm[sm]
        return res

    def getDigitSum(self, x):
        if x < 0:
            return self.getDigitSum(-x)
        res = 0
        while x != 0:
            res += x % 10
            x //= 10
        return res
