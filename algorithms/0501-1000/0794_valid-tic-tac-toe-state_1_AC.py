# medium
# https://leetcode.com/problems/valid-tic-tac-toe-state/
# 1000 ifs and elses
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def checkWin(b, c):
            res = [0, 0, 0, 0]
            for i in range(3):
                j = 0
                while j < 3 and b[i][j] == c:
                    j += 1
                if j == 3:
                    res[0] += 1

                j = 0
                while j < 3 and b[j][i] == c:
                    j += 1
                if j == 3:
                    res[1] += 1

            j = 0
            while j < 3 and b[j][j] == c:
                j += 1
            if j == 3:
                res[2] += 1

            j = 0
            while j < 3 and b[j][2 - j] == c:
                j += 1
            if j == 3:
                res[3] += 1

            return res

        def validWin(res):
            if max(res) > 1:
                return False
            sm = sum(res)
            if sm > 3:
                return False
            if sm < 3:
                return True
            return res[0] == 1 and res[1] == 1

        b = board
        c1 = 0
        c2 = 0
        for i in range(3):
            for j in range(3):
                if b[i][j] == 'X':
                    c1 += 1
                elif b[i][j] == 'O':
                    c2 += 1
        if c1 < c2 or c1 - c2 > 1:
            return False

        r1 = checkWin(b, 'X')
        if not validWin(r1):
            return False

        r2 = checkWin(b, 'O')
        if not validWin(r2):
            return False

        sr1 = sum(r1)
        sr2 = sum(r2)
        if sr1 > 0 and sr2 > 0:
            return False
        if sr1 == 0 and sr2 == 0:
            return True
        return c1 == c2 + 1 if sr1 > 0 else c1 == c2
