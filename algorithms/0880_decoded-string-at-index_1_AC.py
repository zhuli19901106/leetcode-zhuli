# https://leetcode.com/problems/decoded-string-at-index/
# needs some brainy work
from bisect import bisect_right

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        s = S
        if not s[-1].isdigit():
            s += '1'
        n = len(s)
        tp = []
        i = 0
        while i < n:
            j = i
            val = []
            while j < n and s[j].isalpha():
                val.append(s[j])
                j += 1
            i = j
            cnt = 1
            while j < n and s[j].isdigit():
                cnt *= (ord(s[j]) - ord('0'))
                j += 1
            i = j
            tp.append((''.join(val), cnt))

        nt = len(tp)
        ps = [len(tp[0][0]) * tp[0][1]]
        for i in range(1, nt):
            ps.append((ps[-1] + len(tp[i][0])) * tp[i][1])
        
        k = K - 1
        while True:
            i = bisect_right(ps, k)
            step = ps[i] // tp[i][1]
            k %= step
            if i == 0 or k >= ps[i - 1]:
                break

        if i > 0:
            k -= ps[i - 1]
        return tp[i][0][k]
