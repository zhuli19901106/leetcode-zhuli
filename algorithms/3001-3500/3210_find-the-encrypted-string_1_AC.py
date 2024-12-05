# https://leetcode.com/problems/find-the-encrypted-string/
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        if k == 0:
            return s

        a = list(s)
        self.reverse(a, 0, k - 1)
        self.reverse(a, k, n - 1)
        self.reverse(a, 0, n - 1)
        return ''.join(a)

    def reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
