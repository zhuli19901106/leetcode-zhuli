# https://leetcode.com/problems/next-closest-time/
# 1AC, rather verbose and trivial
from bisect import bisect_right

class Solution:
    def nextClosestTime(self, time: str) -> str:
        ds = set([ord(c) - ord('0') for c in time if c.isdigit()])
        h = 0
        res = []
        while h < 24:
            h1 = h // 10
            if not h1 in ds:
                h += 10
                continue

            h2 = h % 10
            if not h2 in ds:
                h += 1
                continue

            m = 0
            while m < 60:
                m1 = m // 10
                if not m1 in ds:
                    m += 10
                    continue

                m2 = m % 10
                if not m2 in ds:
                    m += 1
                    continue

                res.append(h * 60 + m)
                m += 1
            h += 1

        i = time.find(':')
        cur = int(time[:i]) * 60 + int(time[i + 1:])
        i = bisect_right(res, cur)
        i = i if i < len(res) else 0
        return '{:02d}:{:02d}'.format(res[i] // 60, res[i] % 60)
