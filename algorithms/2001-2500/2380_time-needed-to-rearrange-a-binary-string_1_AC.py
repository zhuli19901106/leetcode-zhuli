# medium
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
# BF is trivial, how to do this in O(n)?
# just count how many steps each 0 has to move
# idea is alright, but can't get it to work
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)

        res = 0
        k = n - 1
        last = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0' and k != i:
                last += 1
            else:
                # I still can't fully understand this
                last = max(0, last - 1)

            if s[i] == '1':
                continue

            res = k - i + (last - 1 if k != i else 0)
            k -= 1

        return res
