# medium
# https://leetcode.com/problems/simplified-fractions/
# just bruteforce
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if self.gcd(i, j) != 1:
                    continue
                res.append('{}/{}'.format(j, i))
        return res

    def gcd(self, x, y):
        if x < y:
            return self.gcd(y, x)
        while y != 0:
            x, y = y, x % y
        return x
