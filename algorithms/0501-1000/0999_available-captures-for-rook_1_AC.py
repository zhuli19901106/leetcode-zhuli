# easy
# available-captures-for-rook
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        b = board
        n = len(b)
        found = False
        for i in range(n):
            for j in range(n):
                if b[i][j] == 'R':
                    found = True
                if found:
                    break
            if found:
                break
        ri, rj = i, j
        offset = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        res = 0
        for off in offset:
            i, j = ri, rj
            while True:
                i += off[0]
                j += off[1]
                if i < 0 or i > n - 1 or j < 0 or j > n - 1:
                    break
                if b[i][j] == 'B':
                    break
                if b[i][j] == 'p':
                    res += 1
                    break
        return res
