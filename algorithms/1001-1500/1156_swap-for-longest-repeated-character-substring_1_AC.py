# medium
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
# rather ad-hoc, and boring
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        mc = {}
        rle = []
        s = text
        n = len(s)
        i = 0
        res = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            if s[i] in mc:
                mc[s[i]] += 1
            else:
                mc[s[i]] = 1
            rle.append((s[i], i, j - 1))
            i = j

        nl = len(rle)
        for r in rle:
            cnt = r[2] - r[1] + 1
            if mc[r[0]] > 1:
                cnt += 1
            res = max(res, cnt)

        for i in range(2, nl):
            r1 = rle[i - 2]
            r2 = rle[i]
            if r1[0] != r2[0] or r1[2] + 2 != r2[1]:
                continue
            cnt = r1[2] - r1[1] + 1 + r2[2] - r2[1] + 1
            if mc[r1[0]] > 2:
                cnt += 1
            res = max(res, cnt)
        return res
