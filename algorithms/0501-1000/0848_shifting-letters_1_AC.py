# medium
# https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        R = 26

        s = list(S)
        n = len(s)
        a = shifts[:]
        a[-1] %= R
        for i in range(n - 2, -1, -1):
            a[i] = (a[i] + a[i + 1]) % R
        for i in range(n):
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + a[i]) % R)
        return ''.join(s)
