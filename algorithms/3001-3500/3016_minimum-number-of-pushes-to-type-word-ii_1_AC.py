# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
class Solution:
    def minimumPushes(self, word: str) -> int:
        mm = {}
        for c in word:
            if not c in mm:
                mm[c] = 1
            else:
                mm[c] += 1

        a = [(cnt, c) for c, cnt in mm.items()]
        a.sort(reverse=True)

        res = 0
        idx, push = 0, 1
        for cnt, c in a:
            res += cnt * push
            idx += 1
            if idx == 8:
                idx = 0
                push += 1
        return res
