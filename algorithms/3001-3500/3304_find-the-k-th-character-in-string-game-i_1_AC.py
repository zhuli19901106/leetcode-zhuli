# easy
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        while len(s) < k:
            s1 = []
            for c in s:
                s1.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
            s1 = ''.join(s1)
            s += s1
        return s[k - 1]
