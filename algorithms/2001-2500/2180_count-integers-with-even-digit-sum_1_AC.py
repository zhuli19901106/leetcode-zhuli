# https://leetcode.com/problems/count-integers-with-even-digit-sum/
# brute force for easy
class Solution:
    res = [0]
    MAXN = 1005

    def __init__(self) -> None:
        for i in range(1, self.MAXN + 1):
            sm = 0
            x = i
            while x != 0:
                sm += x % 10
                x //= 10
            self.res.append(self.res[-1] + (1 if sm % 2 == 0 else 0))

    def countEven(self, num: int) -> int:
        return self.res[num]
