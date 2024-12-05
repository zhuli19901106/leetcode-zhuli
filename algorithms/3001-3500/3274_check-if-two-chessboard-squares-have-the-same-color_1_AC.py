# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1, c2 = coordinate1, coordinate2
        return ((ord(c1[0]) - ord(c2[0])) + (ord(c1[1]) - ord(c2[1]))) % 2 == 0
