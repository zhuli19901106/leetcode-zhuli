# https://leetcode.com/problems/number-of-wonderful-substrings/
# got stuck on this for over 1h, really really should be tagged "hard" per se.
# besides, bit manipulation is a teaser if abused.
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        bt = 0
        mm = {0: 1}
        n = len(word)
        for i in range(n):
            idx = ord(word[i]) - ord('a')

            bt ^= (1 << idx)
            if bt in mm:
                res += mm[bt]
            for j in range(10):
                bb = (1 << j)
                # think about it, tricky
                # flip one bit
                bt1 = bt ^ bb
                if bt1 in mm:
                    res += mm[bt1]

            if not bt in mm:
                mm[bt] = 1
            else:
                mm[bt] += 1

        return res
