# easy
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        b = [['' for i in range(3)] for i in range(3)]
        pl = 'XO'
        def check(b):
            for i in range(3):
                if b[i][0] != '' and b[i][0] == b[i][1] and b[i][1] == b[i][2]:
                    return b[i][0]
                if b[0][i] != '' and b[0][i] == b[1][i] and b[1][i] == b[2][i]:
                    return b[0][i]
            if b[0][0] != '' and b[0][0] == b[1][1] and b[1][1] == b[2][2]:
                return b[0][0]
            if b[0][2] != '' and b[0][2] == b[1][1] and b[1][1] == b[2][0]:
                return b[0][2]
            return None

        for i, m in enumerate(moves):
            b[m[0]][m[1]] = pl[i % 2]
            win = check(b)
            if not win is None:
                return 'A' if win == 'X' else 'B'
        if win is None:
            return 'Draw' if len(moves) == 9 else 'Pending'
