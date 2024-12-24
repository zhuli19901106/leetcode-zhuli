# easy
# https://leetcode.com/problems/lexicographically-smallest-palindrome/
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        n = len(a)

        i, j = 0, n - 1
        while i < j:
            if a[i] == a[j]:
                i += 1
                j -= 1
                continue
            if a[i] < a[j]:
                a[j] = a[i]
            else:
                a[i] = a[j]
            i += 1
            j -= 1

        return ''.join(a)
