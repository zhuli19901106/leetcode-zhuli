# medium
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
# convert to base 3 and check for digit 1
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            d = n % 3
            n //= 3
            if d != 0 and d != 1:
                return False
        return True
