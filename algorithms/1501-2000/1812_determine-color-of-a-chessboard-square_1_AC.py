# https://leetcode.com/problems/determine-color-of-a-chessboard-square/
# 1AC
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + int(coordinates[1])) % 2 == 0
