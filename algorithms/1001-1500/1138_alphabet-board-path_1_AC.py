# medium
# https://leetcode.com/problems/alphabet-board-path/
# 1AC, this kind of problems are boring.
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        COL = 5

        def move(ch1, ch2):
            p1 = ord(ch1) - ord('a')
            p2 = ord(ch2) - ord('a')
            r1, c1 = p1 // COL, p1 % COL
            r2, c2 = p2 // COL, p2 % COL
            res = []

            if r1 < r2 and c1 > c2:
                res.append('L' * (c1 - c2))
                res.append('D' * (r2 - r1))
            else:
                chh = 'R' if c1 < c2 else 'L'
                chv = 'D' if r1 < r2 else 'U'
                res.append(chv * abs(r1 - r2))
                res.append(chh * abs(c1 - c2))

            res.append('!')
            return ''.join(res)

        res = []
        c = 'a'
        for c1 in target:
            res.append(move(c, c1))
            c = c1
        return ''.join(res)
