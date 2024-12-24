# medium
# https://leetcode.com/problems/prime-palindrome/
# I don't want another sight of it again
from math import floor, log10

class Solution:
    def __init__(self):
        self.pf = Solution.sievePrime(50000)

    def primePalindrome(self, N: int) -> int:
        def numDigit(x):
            return int(floor(log10(x))) + 1

        def reverseDigit(x):
            y = 0
            while x != 0:
                y = y * 10 + x % 10
                x //= 10
            return y

        def getPal(x, y):
            nd = numDigit(x)
            if y is None:
                return x * (10 ** nd) + reverseDigit(x)
            else:
                return x * (10 ** (nd + 1)) + y * (10 ** nd) + reverseDigit(x)

        def nextPal(n):
            if n < 9:
                return n + 1
            if n == 9:
                return 11

            nd = numDigit(n)
            if nd % 2 == 0:
                x = n // (10 ** (nd // 2))
                y = None
            else:
                x = n // (10 ** (nd // 2 + 1))
                y = n // (10 ** (nd // 2)) % 10
            n1 = getPal(x, y)
            if n1 > n:
                return n1

            if y is None:
                x += 1
            elif y < 9:
                y += 1
            else:
                y = 0
                x += 1
            if x == 10 ** (nd // 2):
                if y is None:
                    x = x // 10
                    y = 0
                else:
                    y = None
            return getPal(x, y)

        x = nextPal(N - 1)
        while True:
            if self.isPrime(x):
                break
            x = nextPal(x)
        return x

    def isPrime(self, x):
        pf = self.pf

        if x < 2:
            return False
        i = 0
        while pf[i] <= x // pf[i]:
            if x % pf[i] == 0:
                return False
            i += 1
        return True

    @staticmethod
    def sievePrime(n):
        a = [True for i in range(n + 1)]
        a[0] = a[1] = False
        i = 2
        while i <= n // i:
            if not a[i]:
                i += 1
                continue
            j = i
            while j <= n // i:
                a[i * j] = False
                j += 1
            i += 1
        pf = [i for i, x in enumerate(a) if x]
        return pf
