# https://leetcode.com/problems/minimum-genetic-mutation/
# simple BFS, not quite efficient, but very intuitive
from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        BS = 'ACGT'

        bst = set(bank)
        n = len(start)
        if n != len(end):
            return -1
        q = deque()
        mm = {}

        mm[start] = 0
        q.append(start)
        while len(q) > 0 and not end in mm:
            s = q.popleft()
            sa = list(s)
            for i in range(n):
                c0 = s[i]
                for c in BS:
                    if c == c0:
                        continue
                    sa[i] = c
                    s1 = ''.join(sa)
                    if (not s1 in mm) and s1 in bst:
                        mm[s1] = mm[s] + 1
                        q.append(s1)
                    sa[i] = c0
        return mm[end] if end in mm else -1
