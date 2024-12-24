# hard
# https://leetcode.com/problems/sliding-puzzle/
# about encoding and searching
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        N, M = 2, 3
        OFFS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        def slide(s, d):
            a = list(s)
            i = s.find('0')

            x, y = i // M, i % M
            x1, y1 = x + OFFS[d][0], y + OFFS[d][1]

            if x1 < 0 or x1 > N - 1 or y1 < 0 or y1 > M - 1:
                return None

            i1 = x1 * M + y1
            a[i], a[i1] = a[i1], a[i]

            return ''.join(a)

        res = {}
        q = deque()

        s0 = '123450'
        t0 = ''.join([chr(ord('0') + x) for x in board[0] + board[1]])

        res[s0] = 0
        q.append((s0, 0))
        while len(q) > 0 and (not t0 in res):
            s, val = q.popleft()

            for i in range(4):
                s1 = slide(s, i)
                if (not s1) or (s1 in res):
                    continue
                res[s1] = val + 1
                q.append((s1, val + 1))

        return res[t0] if t0 in res else -1
