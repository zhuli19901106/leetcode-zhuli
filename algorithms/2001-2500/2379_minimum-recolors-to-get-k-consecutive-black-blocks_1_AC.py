# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# brute-force
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        sm = [0]
        for b in blocks:
            sm.append(sm[-1] + (1 if b == 'B' else 0))

        res = n + 1
        for i in range(k - 1, n):
            res = min(res, max(0, k - (sm[i + 1] - sm[i + 1 - k])))
        return res
