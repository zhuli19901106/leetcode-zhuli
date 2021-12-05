# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# 1AC

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sd = ''.join([str(ord(c) - ord('a') + 1) for c in s])

        for ki in range(k):
            if len(sd) < 2:
                break
            sd = str(sum([int(c) for c in sd]))
        return int(sd)
