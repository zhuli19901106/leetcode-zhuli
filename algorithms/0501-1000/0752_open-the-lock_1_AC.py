# medium
# https://leetcode.com/problems/open-the-lock/
# 1AC, BFS
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s10 = ''.join(map(lambda x: chr(x + ord('0')), range(10)))
        offs = {}
        for i in range(10):
            offs[s10[i]] = [s10[(i + 1) % 10], s10[i - 1]]

        res = {}
        std = set(deadends)

        q = deque()
        s0 = '0000'
        n = len(s0)
        q.append(s0)
        res[s0] = 0
        while len(q) > 0 and (not target in res):
            s = q.popleft()
            if s in std:
                continue
            v = res[s]
            sa = list(s)
            for i, c in enumerate(sa):
                for c1 in offs[c]:
                    sa[i] = c1
                    s1 = ''.join(sa)
                    if not s1 in res:
                        q.append(s1)
                        res[s1] = v + 1
                    sa[i] = c
        if target in res:
            return res[target]
        return -1
