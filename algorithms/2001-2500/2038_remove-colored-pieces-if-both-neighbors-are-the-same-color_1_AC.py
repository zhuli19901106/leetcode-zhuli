# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# what's there to be optimal?

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        s = colors
        n = len(s)
        ca, cb = 0, 0

        i = 0
        while i < n:
            j = i + 1
            while j  < n and s[j] == s[i]:
                j += 1
            if s[i] == 'A':
                ca += max(0, j - i - 2)
            else:
                cb += max(0, j - i - 2)
            i = j

        return ca > cb
