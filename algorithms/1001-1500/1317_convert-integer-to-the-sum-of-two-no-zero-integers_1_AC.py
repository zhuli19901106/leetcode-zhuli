# easy
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution:
    def __init__(self):
        n = 10000
        def hasZero(x):
            if x == 0:
                return True
            while x != 0:
                if x % 10 == 0:
                    return True
                x //= 10
            return False

        self.dp = [hasZero(i) for i in range(n + 1)]

    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while i <= n - i:
            if not self.dp[i] and not self.dp[n - i]:
                return [i, n - i]
            i += 1
        return None
