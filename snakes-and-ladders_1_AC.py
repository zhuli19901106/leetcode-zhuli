# https://leetcode.com/problems/snakes-and-ladders/
# 1AC, BFS
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        msl = {}
        b = board
        n = len(b)
        f = 0
        cnt = 0
        for i in range(n - 1, -1, -1):
            col_range = range(0, n) if f == 0 else range(n - 1, -1, -1)
            for j in col_range:
                cnt += 1
                if b[i][j] == -1:
                    continue
                msl[cnt] = b[i][j]
            f = 1 - f

        q = deque()
        res = {}

        res[1] = 0
        q.append(1)
        while len(q) > 0:
            x = q.popleft()
            i = 1
            while i <= 6 and x + i <= n * n:
                x1 = x + i
                if x1 in msl:
                    x1 = msl[x1]
                if not x1 in res:
                    res[x1] = res[x] + 1
                    q.append(x1)
                i += 1
        return res[n * n] if n * n in res else -1
