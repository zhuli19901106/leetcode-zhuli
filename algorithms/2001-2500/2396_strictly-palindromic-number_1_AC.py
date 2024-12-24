# medium
# https://leetcode.com/problems/strictly-palindromic-number/
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for r in range(2, n - 1):
            a = []
            x = n
            while x != 0:
                a.append(x % r)
                x //= r
            i, j = 0, len(a) - 1
            while i < j:
                if a[i] != a[j]:
                    return False
                i += 1
                j -= 1

        return True
